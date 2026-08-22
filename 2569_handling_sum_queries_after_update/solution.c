// LeetCode 2569 - Handling Sum Queries After Update
// https://leetcode.com/problems/handling-sum-queries-after-update/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int *ones2569;
static bool *lazy2569;
static int *nums1_2569;

static void build2569(int idx, int l, int r) {
    if (l == r) { ones2569[idx] = nums1_2569[l]; return; }
    int m = (l + r) / 2;
    build2569(idx * 2, l, m);
    build2569(idx * 2 + 1, m + 1, r);
    ones2569[idx] = ones2569[idx * 2] + ones2569[idx * 2 + 1];
}

static void apply2569(int idx, int l, int r) {
    ones2569[idx] = (r - l + 1) - ones2569[idx];
    lazy2569[idx] = !lazy2569[idx];
}

static void push2569(int idx, int l, int r) {
    if (lazy2569[idx] && l != r) {
        int m = (l + r) / 2;
        apply2569(idx * 2, l, m);
        apply2569(idx * 2 + 1, m + 1, r);
        lazy2569[idx] = false;
    }
}

static void update2569(int idx, int l, int r, int ql, int qr) {
    if (ql <= l && r <= qr) { apply2569(idx, l, r); return; }
    push2569(idx, l, r);
    int m = (l + r) / 2;
    if (ql <= m) update2569(idx * 2, l, m, ql, qr);
    if (qr > m) update2569(idx * 2 + 1, m + 1, r, ql, qr);
    ones2569[idx] = ones2569[idx * 2] + ones2569[idx * 2 + 1];
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* handleQuery(int* nums1, int nums1Size, int* nums2, int nums2Size, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = nums1Size;
    ones2569 = (int*)calloc((size_t)(4 * n), sizeof(int));
    lazy2569 = (bool*)calloc((size_t)(4 * n), sizeof(bool));
    nums1_2569 = nums1;
    build2569(1, 0, n - 1);
    long long sum2 = 0;
    for (int i = 0; i < nums2Size; i++) sum2 += nums2[i];
    long long* ans = (long long*)malloc((size_t)queriesSize * sizeof(long long));
    int ac = 0;
    for (int i = 0; i < queriesSize; i++) {
        if (queries[i][0] == 1) update2569(1, 0, n - 1, queries[i][1], queries[i][2]);
        else if (queries[i][0] == 2) sum2 += (long long)queries[i][1] * ones2569[1];
        else ans[ac++] = sum2;
    }
    free(ones2569); free(lazy2569);
    *returnSize = ac;
    return ans;
}
