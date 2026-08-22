// LeetCode 3073 - Maximum Increasing Triplet Value
// https://leetcode.com/problems/maximum-increasing-triplet-value/

#include <stdlib.h>
#include <string.h>

static int imax(int a, int b) { return a > b ? a : b; }
static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }

/* BIT storing max value at rank */
typedef struct { int n; int* c; } BIT;
static BIT* bit_new(int n) {
    BIT* b = (BIT*)malloc(sizeof(BIT));
    b->n = n; b->c = (int*)calloc((size_t)(n + 1), sizeof(int));
    return b;
}
static void bit_upd(BIT* b, int x, int v) {
    for (; x <= b->n; x += x & -x) if (v > b->c[x]) b->c[x] = v;
}
static int bit_qry(BIT* b, int x) {
    int s = 0;
    for (; x > 0; x -= x & -x) if (b->c[x] > s) s = b->c[x];
    return s;
}
static int lower_bound(int* a, int n, int x) {
    int l = 0, r = n;
    while (l < r) { int m = (l + r) / 2; if (a[m] < x) l = m + 1; else r = m; }
    return l;
}

int maximumTripletValue(int* nums, int numsSize) {
    int n = numsSize;
    int* right = (int*)malloc((size_t)n * sizeof(int));
    right[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= 0; i--) right[i] = imax(nums[i], right[i + 1]);
    int* st = (int*)malloc((size_t)n * sizeof(int));
    memcpy(st, nums, (size_t)n * sizeof(int));
    qsort(st, (size_t)n, sizeof(int), cmp_int);
    int m = 0;
    for (int i = 0; i < n; i++) if (i == 0 || st[i] != st[i - 1]) st[m++] = st[i];
    BIT* bit = bit_new(m + 2);
    int ans = 0;
    int r0 = lower_bound(st, m, nums[0]) + 1;
    bit_upd(bit, r0, nums[0]);
    for (int j = 1; j < n - 1; j++) {
        if (right[j + 1] > nums[j]) {
            int need = lower_bound(st, m, nums[j]); /* rank of first >= nums[j], want < nums[j] */
            if (need > 0) {
                int val = bit_qry(bit, need);
                if (val > 0) ans = imax(ans, val - nums[j] + right[j + 1]);
            }
        }
        int rj = lower_bound(st, m, nums[j]) + 1;
        bit_upd(bit, rj, nums[j]);
    }
    free(right); free(st); free(bit->c); free(bit);
    return ans;
}
