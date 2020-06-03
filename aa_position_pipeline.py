# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:52:30 2019

@author: think
"""

seq = ''
for line in open('inputseq.txt'):
    if line[0] != '>':
        seq = seq + line.strip()


output = open('inputseq_aa_position.txt', 'w')
for x in range(len(seq)+1):
    if x == 0:
        output.write(' \t')
    elif x < len(seq):
        output.write('%s\t' % (x))
    else:
        output.write('%s\n' % (x))
        
for aa in 'ACDEFGHIKLMNPQRSTVWY':
    pos = []
    mat = [0] * len(seq)
    for i in range(len(seq)):
        if seq[i] == aa:
            pos.append(i+1)
    for j in range(len(seq)):
        if j+1 in pos:
            mat[j] = 1
    mat.insert(0, aa)
    for k in range(len(mat)):
        if k < len(mat)-1:
            output.write('%s\t' % (mat[k]))
        else:
            output.write('%s\n' % (mat[k]))

output.close()
