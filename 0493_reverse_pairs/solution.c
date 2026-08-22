// LeetCode 0493 - Reverse Pairs
// https://leetcode.com/problems/reverse-pairs/

#include <stdlib.h>

static long long mergeSort(int* nums, int start, int end) {
    if (start >= end) {
        return 0;
    }
    const int mid = start + (end - start) / 2;
    long long count = mergeSort(nums, start, mid) + mergeSort(nums, mid + 1, end);
    int j = mid + 1;
    for (int i = start; i <= mid; i++) {
        while (j <= end && (long long)nums[i] > 2LL * nums[j]) {
            j++;
        }
        count += j - (mid + 1);
    }

    int* buffer = (int*)malloc((size_t)(end - start + 1) * sizeof(int));
    int left = start;
    int right = mid + 1;
    int index = 0;
    while (left <= mid && right <= end) {
        if (nums[left] <= nums[right]) {
            buffer[index++] = nums[left++];
        } else {
            buffer[index++] = nums[right++];
        }
    }
    while (left <= mid) {
        buffer[index++] = nums[left++];
    }
    while (right <= end) {
        buffer[index++] = nums[right++];
    }
    for (int offset = 0; offset < end - start + 1; offset++) {
        nums[start + offset] = buffer[offset];
    }
    free(buffer);
    return count;
}

int reversePairs(int* nums, int numsSize) {
    return (int)mergeSort(nums, 0, numsSize - 1);
}
