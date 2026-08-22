// LeetCode 3017 - Count the Number of Houses at a Certain Distance II
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

#include <stdlib.h>

static long long llmin(long long a, long long b) { return a < b ? a : b; }
static long long llmax(long long a, long long b) { return a > b ? a : b; }
static long long llabs_(long long x) { return x < 0 ? -x : x; }

long long* countOfPairs(int n, int x, int y, int* returnSize) {
    if (x > y) { int t = x; x = y; y = t; }
    long long* A = (long long*)calloc((size_t)n, sizeof(long long));
    for (int i = 1; i <= n; i++) {
        A[0] += 2;
        int i0 = (int)llmin((long long)(i - 1), llabs_((long long)(i - y)) + x);
        int i1 = (int)llmin((long long)(n - i), llabs_((long long)(i - x)) + 1 + (n - y));
        int i2 = (int)llmin(llabs_((long long)(i - x)), llabs_((long long)(y - i)) + 1);
        int i3 = (int)llmin(llabs_((long long)(i - x)) + 1, llabs_((long long)(y - i)));
        if (i0 < n) A[i0] -= 1;
        if (i1 < n) A[i1] -= 1;
        if (i2 < n) A[i2] += 1;
        if (i3 < n) A[i3] += 1;
        long long r = llmax((long long)(x - i), 0) + llmax((long long)(i - y), 0);
        int i4 = (int)(r + (y - x) / 2);
        int i5 = (int)(r + (y - x + 1) / 2);
        if (i4 < n) A[i4] -= 1;
        if (i5 < n) A[i5] -= 1;
    }
    for (int i = 1; i < n; i++) A[i] += A[i - 1];
    *returnSize = n;
    return A;
}
