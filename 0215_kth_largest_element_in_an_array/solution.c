// LeetCode 0215 - Kth Largest Element in an Array
// https://leetcode.com/problems/kth-largest-element-in-an-array/

#include <stdlib.h>
#include <time.h>

static void swap(int* nums, int i, int j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}

static int partition(int* nums, int left, int right) {
    int pivotIndex = left + rand() % (right - left + 1);
    swap(nums, pivotIndex, right);
    int store = left;
    for (int i = left; i < right; ++i) {
        if (nums[i] <= nums[right]) {
            swap(nums, store, i);
            store++;
        }
    }
    swap(nums, store, right);
    return store;
}

int findKthLargest(int* nums, int numsSize, int k) {
    srand((unsigned)time(NULL));
    int target = numsSize - k;
    int left = 0;
    int right = numsSize - 1;
    while (left <= right) {
        int pivotIndex = partition(nums, left, right);
        if (pivotIndex == target) {
            return nums[pivotIndex];
        }
        if (pivotIndex < target) {
            left = pivotIndex + 1;
        } else {
            right = pivotIndex - 1;
        }
    }
    return nums[left];
}
