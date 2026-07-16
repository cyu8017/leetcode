// LeetCode 0327 - Count of Range Sum
// https://leetcode.com/problems/count-of-range-sum/

#include <stdlib.h>

static long long mergeSort(
    long long* prefix,
    long long* temp,
    int left,
    int right,
    int lower,
    int upper
) {
    if (left >= right) {
        return 0;
    }
    int mid = left + (right - left) / 2;
    long long count = mergeSort(prefix, temp, left, mid, lower, upper) +
        mergeSort(prefix, temp, mid + 1, right, lower, upper);

    int start = mid + 1;
    int end = mid + 1;
    for (int index = left; index <= mid; index++) {
        while (start <= right && prefix[start] - prefix[index] < lower) {
            start += 1;
        }
        while (end <= right && prefix[end] - prefix[index] <= upper) {
            end += 1;
        }
        count += end - start;
    }

    int tempLeft = left;
    int tempRight = mid + 1;
    int write = left;
    while (tempLeft <= mid && tempRight <= right) {
        if (prefix[tempLeft] <= prefix[tempRight]) {
            temp[write++] = prefix[tempLeft++];
        } else {
            temp[write++] = prefix[tempRight++];
        }
    }
    while (tempLeft <= mid) {
        temp[write++] = prefix[tempLeft++];
    }
    while (tempRight <= right) {
        temp[write++] = prefix[tempRight++];
    }
    for (int index = left; index <= right; index++) {
        prefix[index] = temp[index];
    }
    return count;
}

int countRangeSum(int* nums, int numsSize, int lower, int upper) {
    int prefixSize = numsSize + 1;
    long long* prefix = (long long*)malloc((size_t)prefixSize * sizeof(long long));
    long long* temp = (long long*)malloc((size_t)prefixSize * sizeof(long long));
    prefix[0] = 0;
    for (int index = 0; index < numsSize; index++) {
        prefix[index + 1] = prefix[index] + nums[index];
    }
    long long count = mergeSort(prefix, temp, 0, prefixSize - 1, lower, upper);
    free(prefix);
    free(temp);
    return (int)count;
}
