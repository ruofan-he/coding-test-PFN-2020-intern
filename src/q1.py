#!/usr/bin/env python3
import numpy as np
import sys #計算に関係なし

def count_of_det(a, b, d):
    count = 0
    l = []
    for i1 in [a, b]:
        for i2 in [a, b]:
            for i3 in [a, b]:
                for i4 in [a, b]:
                    for i5 in [a, b]:
                        for i6 in [a, b]:
                            for i7 in [a, b]:
                                for i8 in [a, b]:
                                    for i9 in [a, b]:
                                        arr = np.array(
                                            [[i1,i2,i3],
                                             [i4,i5,i6],
                                             [i7,i8,i9]]
                                        )
                                        det_double = np.linalg.det(arr)
                                        det = round(det_double)
                                        error = abs(det - det_double)
                                        l.append(error)
                                        if det == d:
                                            count = count + 1
    return(count,max(l))

if __name__ == '__main__':

    validation_flag = False
    args = sys.argv
    if len(args) > 1 and args[1] == 'validation':
        validation_flag = True
    
    if validation_flag is True:
        round_error_list = []
        for i in range(-10,11):
            for j in range(-10,11):
                _,error = count_of_det(i,j,0)
                round_error_list.append(error)
        
        print('max rounding errror is {}'.format(max(round_error_list)))
    else:
        with open('q1_out.txt', 'w') as f:
            for line in open('q1_in.txt', 'r'):
                a,b,d=list(map(int,line.split()))
                count, _ = count_of_det(a,b,d)
                print(count, file=f)
            
