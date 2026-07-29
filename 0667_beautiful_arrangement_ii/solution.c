// LeetCode 0667 - Beautiful Arrangement II
// https://leetcode.com/problems/beautiful-arrangement-ii/

#include <stdlib.h>

int* constructArray(int n, int k, int* returnSize) {
    int* result = (int*)malloc((size_t)n * sizeof(int));
    int idx = 0;
    for (int i = 1; i <= n - k; i++) {
        result[idx++] = i;
    }
    int left = n - k + 1;
    int right = n;
    int takeHigh = 1;
    while (left <= right) {
        if (takeHigh) {
            result[idx++] = right--;
        } else {
            result[idx++] = left++;
        }
        takeHigh = !takeHigh;
    }
    *returnSize = n;
    return result;
}
