// LeetCode 2731 - Movement of Robots
// https://leetcode.com/problems/movement-of-robots/

#include <stdlib.h>

static int cmp2731(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int sumDistance(int* nums, int numsSize, char* s, int d) {
    const int MOD = 1000000007;
    int* pos = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++)
        pos[i] = s[i] == 'R' ? nums[i] + d : nums[i] - d;
    qsort(pos, (size_t)numsSize, sizeof(int), cmp2731);
    long long ans = 0, pref = 0;
    for (int i = 0; i < numsSize; i++) {
        ans = (ans + (long long)i * pos[i] % MOD - pref + MOD) % MOD;
        pref = (pref + pos[i]) % MOD;
    }
    free(pos);
    return (int)ans;
}
