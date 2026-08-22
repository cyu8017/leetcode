// LeetCode 2191 - Sort the Jumbled Numbers
// https://leetcode.com/problems/sort-the-jumbled-numbers/

#include <stdlib.h>

typedef struct { int mapped, idx, val; } Pair2191;

static int mapVal2191(int* mapping, int x) {
    if (x == 0) return mapping[0];
    int digits[12], n = 0;
    while (x > 0) { digits[n++] = x % 10; x /= 10; }
    int res = 0;
    for (int i = n - 1; i >= 0; i--) res = res * 10 + mapping[digits[i]];
    return res;
}

static int cmp2191(const void* a, const void* b) {
    const Pair2191 *x = a, *y = b;
    if (x->mapped != y->mapped) return (x->mapped > y->mapped) - (x->mapped < y->mapped);
    return x->idx - y->idx;
}

int* sortJumbled(int* mapping, int mappingSize, int* nums, int numsSize, int* returnSize) {
    (void)mappingSize;
    Pair2191* arr = (Pair2191*)malloc((size_t)numsSize * sizeof(Pair2191));
    for (int i = 0; i < numsSize; i++)
        arr[i] = (Pair2191){mapVal2191(mapping, nums[i]), i, nums[i]};
    qsort(arr, (size_t)numsSize, sizeof(Pair2191), cmp2191);
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) ans[i] = arr[i].val;
    free(arr);
    *returnSize = numsSize;
    return ans;
}
