// LeetCode 3667 - Sort Array By Absolute Value
// https://leetcode.com/problems/sort-array-by-absolute-value/

import java.util.Arrays;

class Solution {
    public int[] sortByAbsoluteValue(int[] nums) {
        Integer[] boxed = new Integer[nums.length];
        for (int i = 0; i < nums.length; i++) boxed[i] = nums[i];
        Arrays.sort(boxed, (a, b) -> Integer.compare(Math.abs(a), Math.abs(b)));
        for (int i = 0; i < nums.length; i++) nums[i] = boxed[i];
        return nums;
    }
}
