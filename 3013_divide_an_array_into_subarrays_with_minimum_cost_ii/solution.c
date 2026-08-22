// LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

#include <stdlib.h>
#include <string.h>

typedef struct { int n; int* c; } BITI;
typedef struct { int n; long long* c; } BITL;

static BITI* biti_new(int n) {
    BITI* b = (BITI*)malloc(sizeof(BITI));
    b->n = n; b->c = (int*)calloc((size_t)(n + 1), sizeof(int));
    return b;
}
static BITL* bitl_new(int n) {
    BITL* b = (BITL*)malloc(sizeof(BITL));
    b->n = n; b->c = (long long*)calloc((size_t)(n + 1), sizeof(long long));
    return b;
}
static void biti_upd(BITI* b, int x, int d) { for (; x <= b->n; x += x & -x) b->c[x] += d; }
static int biti_qry(BITI* b, int x) { int s = 0; for (; x > 0; x -= x & -x) s += b->c[x]; return s; }
static void bitl_upd(BITL* b, int x, long long d) { for (; x <= b->n; x += x & -x) b->c[x] += d; }
static long long bitl_qry(BITL* b, int x) { long long s = 0; for (; x > 0; x -= x & -x) s += b->c[x]; return s; }

static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }
static int lower_bound(int* a, int n, int x) {
    int l = 0, r = n;
    while (l < r) { int m = (l + r) / 2; if (a[m] < x) l = m + 1; else r = m; }
    return l;
}

static int kth(BITI* cnt, int m, int k) {
    int idx = 0;
    for (int bit = 1 << 20; bit; bit >>= 1) {
        int nidx = idx + bit;
        if (nidx <= m && cnt->c[nidx] < k) {
            k -= cnt->c[nidx];
            idx = nidx;
        }
    }
    return idx + 1;
}

static void add_val(BITI* cnt, BITL* sum, int* uniq, int m, int x, int d) {
    int r = lower_bound(uniq, m, x) + 1;
    biti_upd(cnt, r, d);
    bitl_upd(sum, r, (long long)d * x);
}

static long long sum_smallest(BITI* cnt, BITL* sum, int* uniq, int m, int kk) {
    if (kk <= 0) return 0;
    int r = kth(cnt, m, kk);
    int before = biti_qry(cnt, r - 1);
    long long s = bitl_qry(sum, r - 1);
    s += (long long)(kk - before) * uniq[r - 1];
    return s;
}

long long minimumCost(int* nums, int numsSize, int k, int dist) {
    k--;
    int n = numsSize;
    int* uniq = (int*)malloc((size_t)n * sizeof(int));
    memcpy(uniq, nums, (size_t)n * sizeof(int));
    qsort(uniq, (size_t)n, sizeof(int), cmp_int);
    int m = 0;
    for (int i = 0; i < n; i++) if (i == 0 || uniq[i] != uniq[i - 1]) uniq[m++] = uniq[i];

    BITI* cnt = biti_new(m + 2);
    BITL* sum = bitl_new(m + 2);

    int end = dist + 1;
    if (end > n - 1) end = n - 1;
    for (int i = 1; i <= end; i++) add_val(cnt, sum, uniq, m, nums[i], 1);

    int win = end; /* numbers currently in fenwick */
    int kk = k < win ? k : win;
    long long ans = nums[0] + sum_smallest(cnt, sum, uniq, m, kk);

    for (int i = dist + 2; i < n; i++) {
        add_val(cnt, sum, uniq, m, nums[i - dist - 1], -1);
        add_val(cnt, sum, uniq, m, nums[i], 1);
        /* window size stays dist+1 */
        kk = k < (dist + 1) ? k : (dist + 1);
        long long cand = nums[0] + sum_smallest(cnt, sum, uniq, m, kk);
        if (cand < ans) ans = cand;
    }

    free(uniq); free(cnt->c); free(cnt); free(sum->c); free(sum);
    return ans;
}
