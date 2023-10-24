#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script is designed to do some pre-processing for testing my human data set
with PURDY entirely focused on proper fastq format.
Created by David E. Hufnagel on Aug 14, 2023
"""
import sys

inp = open(sys.argv[1])
out = open(sys.argv[2], "w")





#Go through inp, determine whether the line is the 1st, 2nd, 3rd, or 4th for
#  each sequence and ensure it follows the structure 1: @name with no spaces,
#  2: sequence, 3: "+" only, 4: quality ASCII codes
cnt = 1
for line in inp:
    seqLine = cnt % 4
    if seqLine == 1: #line 1 has spaces that need to be removed
        out.write(line.replace(" ","_"))
    elif seqLine == 3: #line 3 has information past the "+" that need to be removed
        out.write(line[0])
        out.write("\n")
    else:
        out.write(line) #lines 2 and 4 seem fine and are therefore left as-is

    cnt += 1









inp.close()
out.close()
