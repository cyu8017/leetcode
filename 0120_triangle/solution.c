// LeetCode 0120 - Triangle
#include <stdlib.h>
int minimumTotal(int** triangle,int triangleSize,int* triangleColSize) {
    int* dp=malloc(triangleSize*sizeof(int)); for(int j=0;j<triangleColSize[triangleSize-1];j++)dp[j]=triangle[triangleSize-1][j];
    for(int i=triangleSize-2;i>=0;i--)for(int j=0;j<=i;j++)dp[j]=triangle[i][j]+(dp[j]<dp[j+1]?dp[j]:dp[j+1]);
    int out=dp[0]; free(dp); return out;
}