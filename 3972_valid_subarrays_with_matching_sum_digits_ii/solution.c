// LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

#include <stdlib.h>

static int lowerBound3972(long long* a, int n, long long x) {
    int lo = 0, hi = n;
    while (lo < hi) { int mid = (lo + hi) / 2; if (a[mid] >= x) hi = mid; else lo = mid + 1; }
    return lo;
}
static int upperBound3972(long long* a, int n, long long x) {
    int lo = 0, hi = n;
    while (lo < hi) { int mid = (lo + hi) / 2; if (a[mid] > x) hi = mid; else lo = mid + 1; }
    return lo;
}

long long countValidSubarrays(int* nums, int numsSize, int x) {
    long long* byR[10];
    int sz[10] = {0}, cap[10] = {0};
    for (int i = 0; i < 10; i++) { byR[i] = NULL; }
    byR[0] = malloc(8 * sizeof(long long)); cap[0] = 8; byR[0][sz[0]++] = 0;
    long long prefix = 0, answer = 0;
    for (int i = 0; i < numsSize; i++) {
        prefix += nums[i];
        int required = (int)((prefix - x) % 10 + 10) % 10;
        long long* values = byR[required];
        int vn = sz[required];
        for (long long power = 1; (long long)x * power <= prefix; power *= 10) {
            long long low = (long long)x * power;
            long long high = (long long)(x + 1) * power - 1;
            long long minPrefix = prefix - high, maxPrefix = prefix - low;
            int left = lowerBound3972(values, vn, minPrefix);
            int right = upperBound3972(values, vn, maxPrefix);
            answer += right - left;
            if (power > prefix / 10) break;
        }
        int rem = (int)(prefix % 10);
        if (sz[rem] == cap[rem]) {
            cap[rem] = cap[rem] ? cap[rem] * 2 : 8;
            byR[rem] = realloc(byR[rem], (size_t)cap[rem] * sizeof(long long));
        }
        byR[rem][sz[rem]++] = prefix;
    }
    for (int i = 0; i < 10; i++) free(byR[i]);
    return answer;
}
