// LeetCode 3592 - Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/

#include <stdlib.h>
int* findCoins(int* numWays, int numWaysSize, int* returnSize) {
    int n=numWaysSize;
    int* dp=(int*)calloc((size_t)n+1,sizeof(int)); dp[0]=1;
    int* coins=(int*)malloc((size_t)n*sizeof(int)); int cn=0;
    for(int amt=1;amt<=n;amt++){
        int ways=numWays[amt-1];
        if(dp[amt]==ways) continue;
        if(dp[amt]+1==ways){
            coins[cn++]=amt;
            for(int x=amt;x<=n;x++) dp[x]+=dp[x-amt];
            if(dp[amt]!=ways){ free(dp); free(coins); *returnSize=0; return NULL; }
            continue;
        }
        free(dp); free(coins); *returnSize=0; return NULL;
    }
    free(dp); *returnSize=cn; return coins;
}
