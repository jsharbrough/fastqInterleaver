import sys
def fastqInterleaver(forwardReads,reverseReads):
    '''Takes two paired-end fastq read files as input and interleaves them. Only paired 
    reads will be retained in the     output fastq. The program will interleave paired 
    forward and reverse reads and write them to standard out, listing forward reads 
    first in the output file to conform with convention. To run, open a Unix 
    environment and type the following:
    
    python fastqInterleaver.py forwardReads reverseReads > out.fastq
    
    Questions about the program should be sent to Joel Sharbrough at 
    jsharbro[at]gmail.com 
    
    I hereby authorize the use, distribution, and modification of this program 
    so long as no profit is made as a result under the MIT License. 
    
    Copyright 2016 Joel Sharbrough. All rights reserved. 
    '''
    
    infile1 = open(forwardReads,'r')
    seqDict = {}
    lineNum = 0
    seqName = ''
    currSeq = ''
    for line in infile1:
        if lineNum == 0:
            if seqName != '':
                seqDict[seqName] = [currSeq]
            lineSplit = line.split(' ')
            seqName = lineSplit[0]
            currSeq = line
            lineNum += 1
        elif lineNum == 1:
            currSeq += line
            lineNum += 1
        elif lineNum == 2:
            currSeq += line
            lineNum += 1
        elif lineNum == 3:
            currSeq += line
            lineNum = 0
    seqDict[seqName] = currSeq
    infile1.close()
    seqName = ''
    currSeq = ''
    infile2 = open(reverseReads,'r')
    lineNum = 0
    readFileName = forwardReads[0:-7]
    for line in infile2:
        if lineNum == 0:
            if seqName != '' and seqName in seqDict:
                seqList = seqDict[seqName]
                sys.stdout.write(seqList[0])
                sys.stdout.write(currSeq)
                del seqDict[seqName]
            lineSplit = line.split(' ')
            seqName = lineSplit[0]
            currSeq = line
            lineNum += 1
        elif lineNum == 1:
            currSeq += line
            lineNum += 1
        elif lineNum == 2:
            currSeq += line
            lineNum += 1
        elif lineNum == 3:
            currSeq += line
            lineNum = 0
    if seqName in seqDict:
        seqList = seqDict[seqName]
        sys.stdout.write(seqList[0])
        sys.stdout.write(currSeq)
    infile2.close()


fastqInterleaver(sys.argv[1],sys.argv[2])
    
    
