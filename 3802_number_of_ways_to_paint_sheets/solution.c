// LeetCode 3802 - Number of Ways to Paint Sheets
// https://leetcode.com/problems/number-of-ways-to-paint-sheets/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int lower_bound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (a[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

int numberOfWays(int n, int* limit, int limitSize) {
    const long long mod = 1000000007;
    qsort(limit, (size_t)limitSize, sizeof(int), cmp_int);
    int* points = (int*)malloc((size_t)(2 * limitSize + 8) * sizeof(int));
    int psz = 0;
    points[psz++] = 1;
    points[psz++] = n;
    for (int i = 0; i < limitSize; i++) {
        int x = limit[i];
        if (x + 1 > 1 && x + 1 < n) points[psz++] = x + 1;
        if (n - x > 1 && n - x < n) points[psz++] = n - x;
    }
    qsort(points, (size_t)psz, sizeof(int), cmp_int);
    int usz = 0;
    for (int i = 0; i < psz; i++) {
        if (usz == 0 || points[usz - 1] != points[i]) points[usz++] = points[i];
    }
    long long ans = 0;
    for (int i = 0; i + 1 < usz; i++) {
        int x = points[i];
        long long a = limitSize - lower_bound(limit, limitSize, x);
        long long b = limitSize - lower_bound(limit, limitSize, n - x);
        int mx = x > n - x ? x : n - x;
        long long same = limitSize - lower_bound(limit, limitSize, mx);
        long long ways = (a * b - same) % mod;
        long long length = points[i + 1] - x;
        ans = (ans + ways * length) % mod;
    }
    if (ans < 0) ans += mod;
    free(points);
    return (int)ans;
}
