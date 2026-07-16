// LeetCode 0119 - Pascal's Triangle II
#include <stdlib.h>
int* getRow(int rowIndex,int* returnSize) {
    *returnSize=rowIndex+1; int* row=malloc(*returnSize*sizeof(int));
    for(int i=0;i<=rowIndex;i++){ row[i]=1; for(int j=i-1;j>0;j--)row[j]+=row[j-1]; } return row;
}