// LeetCode 0215 - Kth Largest Element in an Array
// https://leetcode.com/problems/kth-largest-element-in-an-array/

import java.util.Random;

class Solution {
    private final Random random = new Random();

    public int findKthLargest(int[] nums, int k) {
        int target = nums.length - k;
        int left = 0;
        int right = nums.length - 1;
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

    private int partition(int[] nums, int left, int right) {
        int pivotIndex = left + random.nextInt(right - left + 1);
        swap(nums, pivotIndex, right);
        int store = left;
        for (int i = left; i < right; i++) {
            if (nums[i] <= nums[right]) {
                swap(nums, store, i);
                store++;
            }
        }
        swap(nums, store, right);
        return store;
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
