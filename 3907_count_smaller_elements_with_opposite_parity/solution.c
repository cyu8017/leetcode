// LeetCode 3907 - Count Smaller Elements With Opposite Parity
// https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

#include <stdlib.h>
#include <string.h>

typedef struct { int n; int* c; } BIT3907;

static BIT3907* newBIT3907(int n) {
    BIT3907* b = malloc(sizeof(BIT3907));
    b->n = n;
    b->c = calloc((size_t)(n + 1), sizeof(int));
    return b;
}
static void upd3907(BIT3907* b, int x, int d) {
    for (; x <= b->n; x += x & -x) b->c[x] += d;
}
static int qry3907(BIT3907* b, int x) {
    int s = 0;
    for (; x > 0; x -= x & -x) s += b->c[x];
    return s;
}
static int cmpInt3907(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int* countSmallerOppositeParity(int* nums, int numsSize, int* returnSize) {
    int n = numsSize;
    int* sorted = malloc((size_t)n * sizeof(int));
    memcpy(sorted, nums, (size_t)n * sizeof(int));
    qsort(sorted, (size_t)n, sizeof(int), cmpInt3907);
    int m = 0;
    if (n > 0) {
        m = 1;
        for (int i = 1; i < n; i++) if (sorted[i] != sorted[i - 1]) sorted[m++] = sorted[i];
    }
    BIT3907* bits[2] = { newBIT3907(m), newBIT3907(m) };
    int* ans = malloc((size_t)n * sizeof(int));
    for (int i = n - 1; i >= 0; i--) {
        int lo = 0, hi = m;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (sorted[mid] >= nums[i]) hi = mid;
            else lo = mid + 1;
        }
        int x = lo + 1;
        ans[i] = qry3907(bits[(nums[i] & 1) ^ 1], x - 1);
        upd3907(bits[nums[i] & 1], x, 1);
    }
    free(bits[0]->c); free(bits[0]);
    free(bits[1]->c); free(bits[1]);
    free(sorted);
    *returnSize = n;
    return ans;
}
