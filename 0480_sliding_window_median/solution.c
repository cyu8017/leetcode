// LeetCode 0480 - Sliding Window Median
// https://leetcode.com/problems/sliding-window-median/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int lowerBound(int* arr, int size, int value) {
    int low = 0;
    int high = size;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] < value) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return low;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* medianSlidingWindow(int* nums, int numsSize, int k, int* returnSize) {
    int* window = (int*)malloc((size_t)k * sizeof(int));
    for (int i = 0; i < k; i++) {
        window[i] = nums[i];
    }
    qsort(window, (size_t)k, sizeof(int), cmpInt);

    *returnSize = numsSize - k + 1;
    double* result = (double*)malloc((size_t)(*returnSize) * sizeof(double));
    int out = 0;

    if (k % 2) {
        result[out++] = (double)window[k / 2];
    } else {
        result[out++] = ((double)window[k / 2 - 1] + (double)window[k / 2]) / 2.0;
    }

    for (int index = k; index < numsSize; index++) {
        int outgoing = nums[index - k];
        int pos = lowerBound(window, k, outgoing);
        for (int i = pos; i < k - 1; i++) {
            window[i] = window[i + 1];
        }
        int incoming = nums[index];
        pos = lowerBound(window, k - 1, incoming);
        for (int i = k - 1; i > pos; i--) {
            window[i] = window[i - 1];
        }
        window[pos] = incoming;

        if (k % 2) {
            result[out++] = (double)window[k / 2];
        } else {
            result[out++] = ((double)window[k / 2 - 1] + (double)window[k / 2]) / 2.0;
        }
    }

    free(window);
    return result;
}
