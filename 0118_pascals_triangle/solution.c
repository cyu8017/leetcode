// LeetCode 0118 - Pascal's Triangle
#include <stdlib.h>
int** generate(int numRows,int* returnSize,int** returnColumnSizes) {
    int **a=malloc(numRows*sizeof(*a)); *returnColumnSizes=malloc(numRows*sizeof(int)); *returnSize=numRows;
    for(int i=0;i<numRows;i++){ a[i]=malloc((i+1)*sizeof(int)); (*returnColumnSizes)[i]=i+1; a[i][0]=a[i][i]=1; for(int j=1;j<i;j++)a[i][j]=a[i-1][j-1]+a[i-1][j]; } return a;
}