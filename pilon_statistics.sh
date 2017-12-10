#!/bin/bash


INS=`grep "^000000F" $1 | grep -v "000000F-" | grep -c "\. [ATCG]*$"`
DEL=`grep "^000000F" $1 | grep -v "000000F-" | grep -c "[ATCG] \.$"`
SUB=`grep "^000000F" $1 | grep -v "000000F-" | grep -c " [ATCG]* [ATCG]*$"`
TOT=`grep "^000000F" $1 | grep -v -c "000000F-"` 

echo "Total: $TOT"
echo "Deletions: $DEL"
echo "Insertions: $INS"
echo "Substitutions: $SUB"
