# fastqInterleaver
Takes two fastq read files as input (preferably paired-end reads) and 
interleaves them. Only paired reads will be retained in the output fastq. 
Suffix for the input file must be "fastq" or the original filename will be 
lost and you may encounter errors. To run, open a Unix environment and type 
the following:
    
python fastqInterleaver.py <forwardReads> <reverseReads>
    
The program will interleave paired forward and reverse reads. Forward reads
will be listed first in the output file, conforming to convention. The 
output file will be in fastq format and will use the file handle of the 
forward read file, minus the final character of the file handle prefix.
    
Questions about the program should be sent to Joel Sharbrough at 
jsharbro[at]gmail.com 
    
I hereby authorize the use, distribution, and modification of this program 
so long as no profit is made as a result under the MIT License. 
    
Copyright 2016 Joel Sharbrough. All rights reserved
