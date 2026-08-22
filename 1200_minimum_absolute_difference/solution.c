// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int** minimumAbsDifference(int* arr, int arrSize, int* returnSize, int** returnColumnSizes) {
    qsort(arr, (size_t)arrSize, sizeof(int), cmpInt);
    int best = arr[1] - arr[0];
    for (int i = 1; i + 1 < arrSize; i++) {
        int diff = arr[i + 1] - arr[i];
        if (diff < best) best = diff;
    }
    int count = 0;
    for (int i = 0; i + 1 < arrSize; i++) {
        if (arr[i + 1] - arr[i] == best) count++;
    }
    int** ans = (int**)malloc((size_t)count * sizeof(int*));
    int* cols = (int*)malloc((size_t)count * sizeof(int));
    int idx = 0;
    for (int i = 0; i + 1 < arrSize; i++) {
        if (arr[i + 1] - arr[i] == best) {
            ans[idx] = (int*)malloc(2 * sizeof(int));
            ans[idx][0] = arr[i];
            ans[idx][1] = arr[i + 1];
            cols[idx] = 2;
            idx++;
        }
    }
    *returnSize = count;
    *returnColumnSizes = cols;
    return ans;
}
