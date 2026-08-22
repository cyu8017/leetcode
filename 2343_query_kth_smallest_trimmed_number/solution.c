// LeetCode 2343 - Query Kth Smallest Trimmed Number
// https://leetcode.com/problems/query-kth-smallest-trimmed-number/

#include <stdlib.h>
#include <string.h>

typedef struct { char* s; int i; } Pair;

static int cmpPair(const void* a, const void* b) {
    const Pair* pa = (const Pair*)a;
    const Pair* pb = (const Pair*)b;
    int c = strcmp(pa->s, pb->s);
    if (c != 0) return c;
    return pa->i - pb->i;
}

int* smallestTrimmedNumbers(char** nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int qi = 0; qi < queriesSize; qi++) {
        int k = queries[qi][0], trim = queries[qi][1];
        Pair* arr = (Pair*)malloc((size_t)numsSize * sizeof(Pair));
        for (int i = 0; i < numsSize; i++) {
            int len = (int)strlen(nums[i]);
            arr[i].s = nums[i] + (len - trim);
            arr[i].i = i;
        }
        qsort(arr, (size_t)numsSize, sizeof(Pair), cmpPair);
        ans[qi] = arr[k - 1].i;
        free(arr);
    }
    *returnSize = queriesSize;
    return ans;
}
