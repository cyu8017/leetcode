// LeetCode 3080 - Mark Elements on Array by Performing Queries
// https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int val, idx; } Pair;
static int cmp_pair(const void* a, const void* b) {
    const Pair* pa = (const Pair*)a; const Pair* pb = (const Pair*)b;
    if (pa->val != pb->val) return pa->val - pb->val;
    return pa->idx - pb->idx;
}

long long* unmarkedSumArray(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    long long s = 0;
    for (int i = 0; i < numsSize; i++) s += nums[i];
    bool* mark = (bool*)calloc((size_t)numsSize, sizeof(bool));
    Pair* arr = (Pair*)malloc((size_t)numsSize * sizeof(Pair));
    for (int i = 0; i < numsSize; i++) { arr[i].val = nums[i]; arr[i].idx = i; }
    qsort(arr, (size_t)numsSize, sizeof(Pair), cmp_pair);
    long long* ans = (long long*)malloc((size_t)queriesSize * sizeof(long long));
    int j = 0;
    for (int i = 0; i < queriesSize; i++) {
        int index = queries[i][0], k = queries[i][1];
        if (!mark[index]) { mark[index] = true; s -= nums[index]; }
        for (; k > 0 && j < numsSize; j++) {
            if (!mark[arr[j].idx]) {
                mark[arr[j].idx] = true;
                s -= arr[j].val;
                k--;
            }
        }
        ans[i] = s;
    }
    free(mark); free(arr);
    *returnSize = queriesSize;
    return ans;
}
