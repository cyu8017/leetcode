// LeetCode 2528 - Maximize the Minimum Powered City
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

long long maxPower(int* stations, int stationsSize, int r, int k) {
    int n = stationsSize;
    long long* diff = (long long*)calloc((size_t)(n + 1), sizeof(long long));
    for (int i = 0; i < n; i++) {
        int L = i - r; if (L < 0) L = 0;
        int R = i + r; if (R >= n) R = n - 1;
        diff[L] += stations[i];
        diff[R + 1] -= stations[i];
    }
    long long* power = (long long*)malloc((size_t)n * sizeof(long long));
    long long cur = 0, hi = k;
    for (int i = 0; i < n; i++) {
        cur += diff[i];
        power[i] = cur;
        if (cur > hi) hi = cur;
    }
    hi += k;
    long long* extra = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    long long lo = 0;
    while (lo < hi) {
        long long mid = (lo + hi + 1) / 2;
        memset(extra, 0, (size_t)(n + 1) * sizeof(long long));
        long long have = 0, used = 0;
        bool ok = true;
        for (int i = 0; i < n; i++) {
            have += extra[i];
            long long need = mid - (power[i] + have);
            if (need > 0) {
                used += need;
                if (used > k) { ok = false; break; }
                have += need;
                int end = i + 2 * r;
                if (end + 1 <= n) extra[end + 1] -= need;
            }
        }
        if (ok) lo = mid;
        else hi = mid - 1;
    }
    free(diff); free(power); free(extra);
    return lo;
}
