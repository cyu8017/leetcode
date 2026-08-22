// LeetCode 2971 - Find Polygon With the Largest Perimeter
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

#include <stdlib.h>

static int cmp2971(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

long long largestPerimeter(int* nums, int numsSize) {
    int* arr = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) arr[i] = nums[i];
    qsort(arr, (size_t)numsSize, sizeof(int), cmp2971);
    long long sum = 0;
    for (int i = 0; i < numsSize; i++) sum += arr[i];
    for (int i = numsSize - 1; i >= 2; i--) {
        sum -= arr[i];
        if (sum > arr[i]) {
            long long ans = sum + arr[i];
            free(arr);
            return ans;
        }
    }
    free(arr);
    return -1;
}
