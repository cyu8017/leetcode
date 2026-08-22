// LeetCode 3671 - Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int totalBeauty(int* nums, int numsSize) {
    const int MOD = 1000000007;
    int mx = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > mx) mx = nums[i];
    int* posn = (int*)calloc((size_t)(mx + 1), sizeof(int));
    for (int i = 0; i < numsSize; i++) posn[nums[i]]++;
    int** pos = (int**)malloc((size_t)(mx + 1) * sizeof(int*));
    int* posi = (int*)calloc((size_t)(mx + 1), sizeof(int));
    for (int v = 0; v <= mx; v++) {
        pos[v] = posn[v] ? (int*)malloc((size_t)posn[v] * sizeof(int)) : NULL;
    }
    for (int i = 0; i < numsSize; i++) {
        int v = nums[i];
        pos[v][posi[v]++] = i;
    }
    int* cnt = (int*)calloc((size_t)(mx + 1), sizeof(int));
    int* seq = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int g = 1; g <= mx; g++) {
        int sn = 0;
        for (int m = g; m <= mx; m += g) {
            for (int t = 0; t < posn[m]; t++) seq[sn++] = pos[m][t];
        }
        if (sn == 0) continue;
        qsort(seq, (size_t)sn, sizeof(int), cmpInt);
        int ways = 1;
        for (int t = 0; t < sn; t++) ways = (int)((ways * 2LL) % MOD);
        cnt[g] = (ways - 1 + MOD) % MOD;
    }
    free(seq);
    int ans = 0;
    for (int g = mx; g >= 1; g--) {
        for (int m = 2 * g; m <= mx; m += g) {
            cnt[g] = (cnt[g] - cnt[m] + MOD) % MOD;
        }
        ans = (int)((ans + (long long)cnt[g] * g) % MOD);
    }
    for (int v = 0; v <= mx; v++) free(pos[v]);
    free(pos); free(posn); free(posi); free(cnt);
    return ans;
}
