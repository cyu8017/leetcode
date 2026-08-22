// LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

#include <stdlib.h>
#include <string.h>

long long minOperations(int* nums, int numsSize, int k) {
    long long* evenFreq = calloc((size_t)k, sizeof(long long));
    long long* oddFreq = calloc((size_t)k, sizeof(long long));
    for (int i = 0; i < numsSize; i++) {
        if (i % 2 == 0) evenFreq[nums[i] % k]++;
        else oddFreq[nums[i] % k]++;
    }
long long* evenCost = calloc((size_t)k, sizeof(long long));
    long long* oddCost = calloc((size_t)k, sizeof(long long));
    for (int pass = 0; pass < 2; pass++) {
        long long* freq = pass ? oddFreq : evenFreq;
        long long* res = pass ? oddCost : evenCost;
        long long* doublef = malloc((size_t)(2 * k) * sizeof(long long));
        for (int i = 0; i < 2 * k; i++) doublef[i] = freq[i % k];
        long long* countPrefix = calloc((size_t)(2 * k + 1), sizeof(long long));
        long long* weightedPrefix = calloc((size_t)(2 * k + 1), sizeof(long long));
        for (int i = 0; i < 2 * k; i++) {
            countPrefix[i + 1] = countPrefix[i] + doublef[i];
            weightedPrefix[i + 1] = weightedPrefix[i] + (long long)i * doublef[i];
        }
        int cw = k / 2, cc = (k - 1) / 2;
        for (int t = 0; t < k; t++) {
            long long cnt = countPrefix[t + cw + 1] - countPrefix[t];
            long long sum = weightedPrefix[t + cw + 1] - weightedPrefix[t];
            res[t] += sum - (long long)t * cnt;
            if (cc > 0) {
                cnt = countPrefix[t + k] - countPrefix[t + k - cc];
                sum = weightedPrefix[t + k] - weightedPrefix[t + k - cc];
                res[t] += (long long)(t + k) * cnt - sum;
            }
        }
        free(doublef); free(countPrefix); free(weightedPrefix);
    }
    long long best1 = 1LL << 62, best2 = 1LL << 62;
    int bestIndex = -1;
    for (int i = 0; i < k; i++) {
        long long x = oddCost[i];
        if (x < best1) { best2 = best1; best1 = x; bestIndex = i; }
        else if (x < best2) best2 = x;
    }
    long long ans = 1LL << 62;
    for (int x = 0; x < k; x++) {
        long long other = (x == bestIndex) ? best2 : best1;
        if (evenCost[x] + other < ans) ans = evenCost[x] + other;
    }
    free(evenFreq); free(oddFreq); free(evenCost); free(oddCost);
    return ans;
}
