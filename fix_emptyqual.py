#!/usr/bin/python                                                                                                                                                                             
# Author: Sathish <subramanians@wusm.wustl.edu                                                 \
                                                                                              
import sys,os

infile = open(sys.argv[1],"r")
outfile = open(sys.argv[1].rstrip("fastq")+"corr.fastq","w") 

count = 1
strng = str("FFH>@CCEHHHHD@>CC>EDCBFEHH+>>?EHHHHHDCEDFFGDFHHCCDEHHBFDCF,?B,?FFFFFFFEEEEB,====DEBB@>EEEEEE*88*A:::ACA**::*?C:EA:A?:A?EEAFEAACE=CBCEB<BBB===A<?=:DABBEEFEE@.D@.FFD??C7DDC?.7@<FHHHHF@5AC:HHHEHHFFFHFDFFE5-GDHFC-HGBHGEACFCE88FGDBCEBCHGCDEE>>HHGCFEFFFHHFFEFFFH>@CCEHHHHD@>CC>EDCBFEHH+>>?EHHHHHDCEDFFGDFHHCCDEHHBFDCF,?B,?FFFFFFFEEEEB,====DEBB@>EEEEEE*88*A:::ACA**::*?C:EA:A?:A?EEAFEAACE=CBCEB<BBB===A<?=:DABBEEFEE@.D@.FFD??C7DDC?.7@<FHHHHF@5AC:HHHEHHFFFHFDFFE5-GDHFC-HGBHGEACFCE88FGDBCEBCHGCDEE>>HHGCFEFFFHHFFEF<?=:DABBEEFEE@.D@.FFD??C7DDC?.7@<FHHHHF@5AC:HHHEHHFFFHFDFFE5-GDHFC-HGBHGEACFCE88FGDBCEBCHGCDEE>>HHGCFEFFFHHFE>>HHGCFEFFFHHFFEF<?=:DABBEEFEE@.D@.FFD??C7DDC?.7@<FHHHHF@5AC:HHHEHHFFFHFDFFE5-GDHFC-HGBHGEACFCE88FGDBCEBCHGCDEE>>HHGCFEFFFHHFE>>HHGCFEFFFHHFFEF<?=:DABBEEFEE@.D@.FFD??C7DDC?.7@<FHHHHF@5AC:HHHEHHFFFHFDFFE5-GDHFC-HGBHGEACFCE88FGDBCEBCHGCDEE>>HHGCFEFFFHHFE>>HHGCFEFFFHHFFEF<?=:DABBEEFEE@.D@.FFD??C7DDC?.7@<FHHHHF@5AC:HHHEHHFFFHFDFFE5-GDHFC-HGBHG\EACFCE88FGDBCEBCHGCDEE>>HHGCFEFFFHHF")

quallen=0

for line in infile:
    if  count%4!=0:
        outfile.write(line)
        if count%2==0:
            quallen=line.rstrip("\n").__len__()
    else:
        outfile.write(strng[0:quallen]+"\n")
    count = count + 1
        


