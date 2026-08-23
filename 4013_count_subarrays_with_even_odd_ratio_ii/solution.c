// LeetCode 4013 - Count Subarrays With Even Odd Ratio II
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

#include <stdlib.h>
#include <stdint.h>
#include <string.h>

typedef struct {
    int n;
    int* c;
} BIT4013;

static void bitUpdate4013(BIT4013* bit, int x, int delta) {
    for (; x <= bit->n; x += x & -x) bit->c[x] += delta;
}

static int bitQuery4013(BIT4013* bit, int x) {
    int sum = 0;
    for (; x > 0; x -= x & -x) sum += bit->c[x];
    return sum;
}

static int cmpI64(const void* a, const void* b) {
    int64_t x = *(const int64_t*)a, y = *(const int64_t*)b;
    return (x > y) - (x < y);
}

static int lowerBoundI64(int64_t* a, int n, int64_t v) {
    int l = 0, r = n;
    while (l < r) {
        int mid = (l + r) >> 1;
        if (a[mid] >= v) r = mid;
        else l = mid + 1;
    }
    return l;
}

long long countRatioSubarrays(int* nums, int numsSize, int a, int b) {
    int n = numsSize;
    int64_t* s = (int64_t*)malloc((size_t)(n + 1) * sizeof(int64_t));
    s[0] = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] % 2 == 1) s[i + 1] = s[i] + (int64_t)a;
        else s[i + 1] = s[i] - (int64_t)b;
    }

    int64_t* st = (int64_t*)malloc((size_t)(n + 1) * sizeof(int64_t));
    memcpy(st, s, (size_t)(n + 1) * sizeof(int64_t));
    qsort(st, (size_t)(n + 1), sizeof(int64_t), cmpI64);

    int un = 0;
    for (int i = 0; i <= n; i++) {
        if (un == 0 || st[un - 1] != st[i]) st[un++] = st[i];
    }

    BIT4013 bit;
    bit.n = un + 1;
    bit.c = (int*)calloc((size_t)(bit.n + 1), sizeof(int));

    int64_t ans = 0;
    for (int i = 0; i <= n; i++) {
        int x = lowerBoundI64(st, un, s[i]) + 1;
        ans += (int64_t)bitQuery4013(&bit, x);
        bitUpdate4013(&bit, x, 1);
    }

    free(s);
    free(st);
    free(bit.c);
    return ans;
}
