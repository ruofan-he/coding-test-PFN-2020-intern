#!/usr/bin/env python3
import numpy as np
import sys #計算に関係なし

def validation_of_count(k,p,q): #愚直に解く関数(非常に重い)
    S = ['a','b','c']
    for i in range(3,k):
        S[i % 3] = S[(i-3) % 3] + S[(i-2) % 3] + S[(i-1) % 3]
    s = S[(k-1) % 3][p-1:q]
    return(s.count('a'), s.count('b'), s.count('c'))

def count_of_abc(k,p,q):
    string_length = [1,1,1]
    for i in range(3,k):
        string_length.append(string_length[i-3] + string_length[i-2] + string_length[i-1])
        
    memory = [None] * (k+3)
    memory[0] = [1,0,0]
    memory[1] = [0,1,0]
    memory[2] = [0,0,1]
    
    def recursive(k,p,q,string_length):
        
        if k < 4:
            if p == 1 and q == 1:
                return(memory[k-1])
            else:
                return([0,0,0])
        
        if p == 1 and q == string_length[k-1]:
            if memory[k-1] is not None:
                return(memory[k-1])
        
        segments = [string_length[k-4],string_length[k-3],string_length[k-2]]
        cum = 0
        separation = []
        for i in segments:
            l = []
            if cum + i < p:
                separation.append(l)
                cum = cum + i
                continue
            if cum + 1 > q:
                separation.append(l)
                cum = cum + i
                continue
            l.append(max(p-cum,1))
            l.append(min(q-cum,i))
            cum = cum + i
            separation.append(l)
            
        total_a = 0
        total_b = 0
        total_c = 0
            
        for i, sep in enumerate(separation):
            if len(sep) != 0:
                a,b,c = recursive(k-3+i, sep[0], sep[1], string_length)
                total_a = total_a + a
                total_b = total_b + b
                total_c = total_c + c
        
        if p == 1 and q == string_length[k-1]:
            memory[k-1] = [total_a,total_b,total_c]
        return(total_a,total_b,total_c)
    
    return(recursive(k,p,q,string_length))


if __name__ == '__main__':

    validation_flag = False
    args = sys.argv
    if len(args) > 1 and args[1] == 'validation':
        validation_flag = True
    
    if validation_flag is True:
        print('validation')
        string_length = [1,1,1]
        for i in range(3,15):
            string_length.append(string_length[i-3] + string_length[i-2] + string_length[i-1])
        fault_flag = False
        for k in range(1,15):
            for p in range(1,string_length[k-1]):
                for q in range(p,string_length[k-1]):
                    if validation_of_count(k,p,q) != count_of_abc(k,p,q):
                        fault_flag = True
                        print('error at {},{},{}'.format(k,p,q))
                        break
                if fault_flag:
                    break
            if fault_flag:
                break
        print('validation complete')
        if not fault_flag:
            print('without error')
            
    else:
        with open('q2_out.txt', 'w') as f:
            for line in open('q2_in.txt', 'r'):
                k,p,q=list(map(int,line.split()))
                a,b,c = count_of_abc(k,p,q)
                print('a:{},b:{},c:{}'.format(a,b,c), file=f)
            
