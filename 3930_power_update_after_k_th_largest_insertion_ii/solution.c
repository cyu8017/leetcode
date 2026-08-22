// LeetCode 3930 - Power Update After K-th Largest Insertion II
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/

#include <stdlib.h>
#include <string.h>

enum { MOD3930 = 1000000007LL };
static int* bit3930;
static int m3930;
static int* uniq3930;

static int cmpInt3930(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}
static long long powmod3930(long long a, long long e) {
    long long res = 1;
    while (e > 0) {
        if (e & 1) res = res * a % MOD3930;
        a = a * a % MOD3930;
        e >>= 1;
    }
    return res;
}
static void add3930(int i) {
    for (; i <= m3930; i += i & -i) bit3930[i]++;
}
static int kth3930(int rank) {
    int idx = 0, step = 1;
    while ((step << 1) < m3930 + 1) step <<= 1;
    for (; step > 0; step >>= 1) {
        int next = idx + step;
        if (next <= m3930 && bit3930[next] < rank) {
            idx = next;
            rank -= bit3930[next];
        }
    }
    return uniq3930[idx];
}
static int lower3930(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (a[mid] >= x) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}

int* powerUpdate(int* nums, int numsSize, int p, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int total = numsSize + queriesSize;
    int* vals = malloc((size_t)total * sizeof(int));
    memcpy(vals, nums, (size_t)numsSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) vals[numsSize + i] = queries[i][0];
    qsort(vals, (size_t)total, sizeof(int), cmpInt3930);
    m3930 = 0;
    for (int i = 0; i < total; i++) {
        if (m3930 == 0 || vals[m3930 - 1] != vals[i]) vals[m3930++] = vals[i];
    }
    uniq3930 = vals;
    bit3930 = calloc((size_t)(m3930 + 1), sizeof(int));
    for (int i = 0; i < numsSize; i++) add3930(lower3930(vals, m3930, nums[i]) + 1);
    int* ans = malloc((size_t)queriesSize * sizeof(int));
    int size = numsSize;
    long long cur = p;
    for (int i = 0; i < queriesSize; i++) {
        add3930(lower3930(vals, m3930, queries[i][0]) + 1);
        size++;
        int x = kth3930(size - queries[i][1] + 1);
        cur = powmod3930(cur, x);
        ans[i] = (int)cur;
    }
    free(vals); free(bit3930);
    *returnSize = queriesSize;
    return ans;
}
