// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

#include <string.h>
#include <stdlib.h>

static int bitsPop(int x) { int c = 0; while (x) { c += x & 1; x >>= 1; } return c; }

static int red3352[801];
static char* s3352;
static int n3352, k3352, mod3352;
static int* memo3352;
static char* seen3352;

static int dfs3352(int pos, int tight, int ones) {
    if (pos == n3352) {
        if (ones == 0) return 0;
        return red3352[ones] <= k3352 - 1 ? 1 : 0;
    }
    int id = ((pos * 2 + tight) * 801 + ones);
    if (seen3352[id]) return memo3352[id];
    int up = tight ? s3352[pos] - '0' : 1;
    int ans = 0;
    for (int d = 0; d <= up; d++) {
        int nt = tight && d == up;
        ans = (ans + dfs3352(pos + 1, nt, ones + d)) % mod3352;
    }
    seen3352[id] = 1; memo3352[id] = ans; return ans;
}

int countKReducibleNumbers(char* s, int k) {
    mod3352 = 1000000007;
    red3352[1] = 0;
    for (int i = 2; i <= 800; i++) red3352[i] = 1 + red3352[bitsPop(i)];
    s3352 = s; n3352 = (int)strlen(s); k3352 = k;
    memo3352 = (int*)malloc((n3352 + 1) * 2 * 801 * sizeof(int));
    seen3352 = (char*)calloc((n3352 + 1) * 2 * 801, 1);
    int ans = dfs3352(0, 1, 0);
    free(memo3352); free(seen3352);
    return ans;
}
