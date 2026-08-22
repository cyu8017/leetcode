// LeetCode 3665 - Twisted Mirror Path Count
// https://leetcode.com/problems/twisted-mirror-path-count/

#include <stdlib.h>
#include <stdbool.h>
#define MOD 1000000007
int uniquePaths(int** grid, int gridSize, int* gridColSize) {
    int m=gridSize,n=gridColSize[0];
    int** dp=(int**)malloc((size_t)m*sizeof(int*)); for(int i=0;i<m;i++) dp[i]=(int*)calloc((size_t)n,sizeof(int));
    if(grid[0][0]==1){ for(int i=0;i<m;i++) free(dp[i]); free(dp); return 0; }
    dp[0][0]=1;
    for(int i=0;i<m;i++) for(int j=0;j<n;j++){
        if(grid[i][j]==1||dp[i][j]==0) continue;
        for(int pass=0;pass<2;pass++){
            int di=pass?1:0, dj=pass?0:1; int ni=i+di,nj=j+dj;
            while(ni>=0&&nj>=0&&ni<m&&nj<n&&grid[ni][nj]==1){ if(dj==1){di=1;dj=0;} else {di=0;dj=1;} ni+=di; nj+=dj; }
            if(ni>=0&&nj>=0&&ni<m&&nj<n) dp[ni][nj]=(dp[ni][nj]+dp[i][j])%MOD;
        }
    }
    int ans=dp[m-1][n-1]; for(int i=0;i<m;i++) free(dp[i]); free(dp); return ans;
}
