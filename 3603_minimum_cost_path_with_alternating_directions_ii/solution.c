// LeetCode 3603 - Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

#include <stdlib.h>
long long minCost(int m, int n, int** waitCost, int waitCostSize, int* waitCostColSize) {
    (void)waitCostSize;(void)waitCostColSize;
    long long** dp=(long long**)malloc((size_t)m*sizeof(long long*));
    for(int i=0;i<m;i++){ dp[i]=(long long*)malloc((size_t)n*sizeof(long long)); for(int j=0;j<n;j++) dp[i][j]=1LL<<62; }
    #define ENTRY(i,j) ((long long)((i)+1)*((j)+1))
    dp[0][0]=ENTRY(0,0);
    for(int i=0;i<m;i++) for(int j=0;j<n;j++){
        if(i==0&&j==0) continue;
        if(i>0){ long long cand=dp[i-1][j]+ENTRY(i,j); if(!(i-1==0&&j==0)) cand+=waitCost[i-1][j]; if(cand<dp[i][j]) dp[i][j]=cand; }
        if(j>0){ long long cand=dp[i][j-1]+ENTRY(i,j); if(!(i==0&&j-1==0)) cand+=waitCost[i][j-1]; if(cand<dp[i][j]) dp[i][j]=cand; }
    }
    long long ans=dp[m-1][n-1];
    for(int i=0;i<m;i++) free(dp[i]); free(dp);
    return ans;
}
