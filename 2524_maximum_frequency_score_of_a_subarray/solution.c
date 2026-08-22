// LeetCode 2524 - Maximum Frequency Score of a Subarray
// https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

#include <stdlib.h>
#include <string.h>

enum { MOD2524 = 1000000007 };

static long long modPow2524(long long a, long long e) {
    long long res = 1;
    a %= MOD2524;
    while (e > 0) {
        if (e & 1) res = res * a % MOD2524;
        a = a * a % MOD2524;
        e >>= 1;
    }
    return res;
}

typedef struct { int key, val; } KV2524;

static int findKV(KV2524* a, int n, int key) {
    for (int i = 0; i < n; i++) if (a[i].key == key) return i;
    return -1;
}

int maxFrequencyScore(int* nums, int numsSize, int k) {
    KV2524* freq = (KV2524*)malloc((size_t)(k + 5) * sizeof(KV2524));
    int fc = 0;
    long long score = 0, best = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        int idx = findKV(freq, fc, x);
        int c = idx >= 0 ? freq[idx].val : 0;
        if (c > 0) score = (score - modPow2524(x, c) + MOD2524) % MOD2524;
        if (idx < 0) { freq[fc].key = x; freq[fc].val = 1; fc++; }
        else freq[idx].val = c + 1;
        score = (score + modPow2524(x, c + 1)) % MOD2524;

        if (i >= k) {
            int y = nums[i - k];
            idx = findKV(freq, fc, y);
            c = freq[idx].val;
            score = (score - modPow2524(y, c) + MOD2524) % MOD2524;
            if (c == 1) {
                freq[idx] = freq[fc - 1];
                fc--;
            } else {
                freq[idx].val = c - 1;
                score = (score + modPow2524(y, c - 1)) % MOD2524;
            }
        }
        if (i >= k - 1 && score > best) best = score;
    }
    free(freq);
    return (int)best;
}
