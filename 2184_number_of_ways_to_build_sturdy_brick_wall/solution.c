// LeetCode 2184 - Number of Ways to Build Sturdy Brick Wall
// https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

#include <stdlib.h>
#include <string.h>

#define MOD2184 1000000007

static int* masks2184;
static int mcnt2184;
static int* bricks2184;
static int bsz2184;

static void gen2184(int remain, int mask) {
    if (remain == 0) {
        masks2184[mcnt2184++] = mask;
        return;
    }
    for (int i = 0; i < bsz2184; i++) {
        int b = bricks2184[i];
        if (b <= remain) {
            int nm = mask;
            if (remain - b > 0) nm |= 1 << (remain - b);
            gen2184(remain - b, nm);
        }
    }
}

int buildWall(int height, int width, int* bricks, int bricksSize) {
    bricks2184 = bricks; bsz2184 = bricksSize;
    masks2184 = (int*)malloc(100000 * sizeof(int));
    mcnt2184 = 0;
    gen2184(width, 0);
    int m = mcnt2184;
    int** compat = (int**)malloc((size_t)m * sizeof(int*));
    int* clen = (int*)calloc((size_t)m, sizeof(int));
    int* ccap = (int*)calloc((size_t)m, sizeof(int));
    for (int i = 0; i < m; i++) {
        compat[i] = NULL;
        for (int j = 0; j < m; j++) {
            if ((masks2184[i] & masks2184[j]) == 0) {
                if (clen[i] == ccap[i]) {
                    ccap[i] = ccap[i] ? ccap[i] * 2 : 4;
                    compat[i] = (int*)realloc(compat[i], (size_t)ccap[i] * sizeof(int));
                }
                compat[i][clen[i]++] = j;
            }
        }
    }
    int* dp = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) dp[i] = 1;
    for (int h = 1; h < height; h++) {
        int* ndp = (int*)calloc((size_t)m, sizeof(int));
        for (int i = 0; i < m; i++)
            for (int t = 0; t < clen[i]; t++) {
                int j = compat[i][t];
                ndp[j] = (ndp[j] + dp[i]) % MOD2184;
            }
        free(dp); dp = ndp;
    }
    int ans = 0;
    for (int i = 0; i < m; i++) ans = (ans + dp[i]) % MOD2184;
    for (int i = 0; i < m; i++) free(compat[i]);
    free(compat); free(clen); free(ccap); free(dp); free(masks2184);
    return ans;
}
