// LeetCode 0493 - Reverse Pairs
// https://leetcode.com/problems/reverse-pairs/

import java.util.Arrays;

class Solution {
    public int reversePairs(int[] nums) {
        return mergeSort(nums, 0, nums.length - 1);
    }

    private int mergeSort(int[] nums, int start, int end) {
        if (start >= end) {
            return 0;
        }
        int mid = (start + end) / 2;
        int count = mergeSort(nums, start, mid) + mergeSort(nums, mid + 1, end);
        int j = mid + 1;
        for (int i = start; i <= mid; i++) {
            while (j <= end && nums[i] > 2L * nums[j]) {
                j++;
            }
            count += j - (mid + 1);
        }
        int[] slice = Arrays.copyOfRange(nums, start, end + 1);
        Arrays.sort(slice);
        System.arraycopy(slice, 0, nums, start, slice.length);
        return count;
    }
}
