// LeetCode 3181 - Maximum Total Reward Using Operations II
// https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

#include <stdlib.h>
#include <string.h>

static int cmp3181(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int maxTotalReward(int* rewardValues, int rewardValuesSize) {
    qsort(rewardValues, rewardValuesSize, sizeof(int), cmp3181);
    int n = 0;
    for (int i = 0; i < rewardValuesSize; i++)
        if (n == 0 || rewardValues[i] != rewardValues[n - 1])
            rewardValues[n++] = rewardValues[i];
    int maxv = rewardValues[n - 1];
    int bits = maxv * 2 + 2;
    int limbs = (bits + 63) / 64;
    unsigned long long* f = calloc(limbs, sizeof(unsigned long long));
    unsigned long long* tmp = calloc(limbs, sizeof(unsigned long long));
    f[0] = 1;
    for (int ti = 0; ti < n; ti++) {
        int v = rewardValues[ti];
        memset(tmp, 0, limbs * sizeof(unsigned long long));
        for (int i = 0; i < limbs; i++) {
            unsigned long long x = f[i];
            int base = i * 64;
            if (base >= v) x = 0;
            else if (base + 64 > v) {
                int keep = v - base;
                x &= (keep == 64) ? ~0ULL : ((1ULL << keep) - 1);
            }
            if (!x) continue;
            int sh = v / 64, sb = v % 64, dest = i + sh;
            if (sb == 0) { if (dest < limbs) tmp[dest] |= x; }
            else {
                if (dest < limbs) tmp[dest] |= x << sb;
                if (dest + 1 < limbs) tmp[dest + 1] |= x >> (64 - sb);
            }
        }
        for (int i = 0; i < limbs; i++) f[i] |= tmp[i];
    }
    int ans = 0;
    for (int i = limbs - 1; i >= 0; i--) if (f[i]) { ans = i * 64 + (63 - __builtin_clzll(f[i])); break; }
    free(f); free(tmp);
    return ans;
}
