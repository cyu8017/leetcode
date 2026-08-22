// LeetCode 0658 - Find K Closest Elements
// https://leetcode.com/problems/find-k-closest-elements/

#include <stdlib.h>

int* findClosestElements(int* arr, int arrSize, int k, int x, int* returnSize) {
    int left = 0, right = arrSize - k;
    while (left < right) {
        int mid = (left + right) / 2;
        if (x - arr[mid] > arr[mid + k] - x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    int* result = (int*)malloc((size_t)k * sizeof(int));
    for (int i = 0; i < k; i++) {
        result[i] = arr[left + i];
    }
    *returnSize = k;
    return result;
}
