// LeetCode 3759 - Count Elements With At Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int countElements(int* nums, int numsSize, int k) {
    int n = numsSize;
    if (k == 0) return n;
    int* a = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) a[i] = nums[i];
    qsort(a, (size_t)n, sizeof(int), cmpInt);
    int ans = 0;
    for (int i = 0; i < n - k; i++) if (a[n - k] > a[i]) ans++;
    free(a);
    return ans;
}
