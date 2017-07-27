# fastqInterleaver
Takes two paired-end fastq read files as input and interleaves them. Only paired 
reads will be retained in the output fastq. The program will interleave paired 
forward and reverse reads and write them to standard out, listing forward reads 
first in the output file to conform with convention.To run, open a Unix 
environment and type the following:
    
python fastqInterleaver.py forwardReads reverseReads > out.fastq
    
Questions about the program should be sent to Joel Sharbrough at 
jsharbro[at]gmail.com 
    
I hereby authorize the use, distribution, and modification of this program 
so long as no profit is made as a result under the MIT License. 
    
Copyright 2016 Joel Sharbrough. All rights reserved.
