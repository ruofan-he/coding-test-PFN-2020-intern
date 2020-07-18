#!/usr/bin/env python3
import numpy as np
import sys #計算に関係なし


def validation_of_count(n,a1): #検証用の愚直に解く関数(結構重い)
    seat = [999999999999] * n
    count = 0
    l = []
    for i in range(n):
        ai = None
        if i == 0:
            ai = a1
        else:
            ai = np.argmax(seat) + 1
        seat[ai-1] = 0
        for distance, a in enumerate(range(ai, 0, -1)): #現実の席番号に使用ぞ ai~1まで
            if seat[a-1] < distance:
                break
            seat[a-1] = distance
        for distance, a in enumerate(range(ai,n+1)): #現実の席番号に使用ぞ ai~n
            if seat[a-1] < distance:
                break
            seat[a-1] = distance
        if (i+1)%2 == 0:
            count = count + ai
        l.append(ai)
    return(l)  # 座わられる順の席番号のリスト



class Mytree:
    range_of_segment = None
    center = None
    child = None
    
    def __init__(self,range_of_segment,center):
        self.range_of_segment = range_of_segment
        self.center = center
        self.child = []
        self.score = None
        
    def append(self, child):
        self.child.append(child)

def count_of_seat(n,a1):
    range_of_segment = [1,n]
    center = a1
    root = Mytree(range_of_segment, center)

    def make_tree(k,tree):
        left_edge = tree.range_of_segment[0]
        right_edge = tree.range_of_segment[1]
        center = tree.center
        if k == 1 or k == 0:
            tree.score = right_edge - left_edge
        else:
            tree.score = int((right_edge - left_edge -(right_edge - left_edge) % 2)/2) 
        if left_edge == right_edge:
            return
        
        if left_edge != center:
            l = left_edge
            r = center - 1
            child_segment = [l,r]
            child_center = int((l + r - (r-l)%2 )/2)
            if k == 0:
                child_center = l
            left_child = Mytree(child_segment,child_center)
            tree.append(left_child)
            make_tree(k+1, left_child)
        #前後注意
        if right_edge != center:
            l = center + 1
            r = right_edge
            child_segment = [l,r]
            child_center = int((l + r - (r-l)%2 )/2)
            if k == 0:
                child_center = r
            right_child = Mytree(child_segment,child_center)
            tree.append(right_child)
            make_tree(k+1, right_child)
            
        return
    
    make_tree(0, root)
    
    l = []
    l_score = []
    def ranking(tree,l):
        l.append(tree.center)
        l_score.append(tree.score)
        for child in tree.child:
            ranking(child,l)
    ranking(root,l)
    l = [l[i] for i in np.argsort(-np.array(l_score),kind = 'mergesort')]
    
    count = 0
    for i in range(n):
        if (i+1)%2 == 0:
            count = count + l[i]
    return(count, l)




if __name__ == '__main__':

    validation_flag = False
    args = sys.argv
    if len(args) > 1 and args[1] == 'validation':
        validation_flag = True
    
    if validation_flag is True:
        print('validation')
        fault_flag = False
        for n in range(1,101):
            for a1 in range(1,n+1):
                _ , l = count_of_seat(n,a1)
                val_l = validation_of_count(n,a1)
                if l != val_l:
                    print('error at ({},{})'.format(n,a1))
                    fault_flag = True
                    break
            if fault_flag:
                break
        print('validation complete')
        if not fault_flag:
            print('without error')
        
    else:
        with open('q3_out.txt', 'w') as f:
            for line in open('q3_in.txt', 'r'):
                n,a1=list(map(int,line.split()))
                count , _ = count_of_seat(n,a1)
                print(count, file=f)
            
