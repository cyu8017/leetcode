// LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

int maxCount(int* banned, int bannedSize, int n, long long maxSum) {
    qsort(banned, (size_t)bannedSize, sizeof(int), cmpInt);
    int* uniq = (int*)malloc((size_t)bannedSize * sizeof(int));
    int u = 0;
    for (int i = 0; i < bannedSize; i++) {
        int x = banned[i];
        if (x >= 1 && x <= n && (u == 0 || uniq[u - 1] != x)) uniq[u++] = x;
    }
    int ans = 0;
    int prev = 0;
    long long remain = maxSum;
    long long* segs_l = (long long*)malloc((size_t)(u + 1) * sizeof(long long));
    long long* segs_r = (long long*)malloc((size_t)(u + 1) * sizeof(long long));
    int sc = 0;
    for (int i = 0; i < u; i++) {
        long long l = (long long)prev + 1;
        long long r = (long long)uniq[i] - 1;
        if (l <= r) { segs_l[sc] = l; segs_r[sc] = r; sc++; }
        prev = uniq[i];
    }
    {
        long long l = (long long)prev + 1;
        long long r = (long long)n;
        if (l <= r) { segs_l[sc] = l; segs_r[sc] = r; sc++; }
    }
    for (int s = 0; s < sc && remain > 0; s++) {
        long long l = segs_l[s], r = segs_r[s];
        long long lo = l, hi = r, best = l - 1;
        while (lo <= hi) {
            long long mid = (lo + hi) / 2;
            long long cnt = mid - l + 1;
            long long sum = (l + mid) * cnt / 2;
            if (sum <= remain) { best = mid; lo = mid + 1; }
            else hi = mid - 1;
        }
        if (best >= l) {
            long long cnt = best - l + 1;
            ans += (int)cnt;
            remain -= (l + best) * cnt / 2;
        }
    }
    free(segs_l);
    free(segs_r);
    free(uniq);
    return ans;
}
