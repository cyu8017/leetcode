// LeetCode 0912 - Sort an Array
// https://leetcode.com/problems/sort-an-array/

import java.util.Arrays;

class Solution {
    public int[] sortArray(int[] nums) {
        if (nums.length <= 1) return nums;
        int mid = nums.length / 2;
        int[] left = Arrays.copyOfRange(nums, 0, mid);
        int[] right = Arrays.copyOfRange(nums, mid, nums.length);
        left = sortArray(left);
        right = sortArray(right);
        int[] merged = new int[nums.length];
        int i = 0, j = 0, k = 0;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) merged[k++] = left[i++];
            else merged[k++] = right[j++];
        }
        while (i < left.length) merged[k++] = left[i++];
        while (j < right.length) merged[k++] = right[j++];
        return merged;
    }
}
