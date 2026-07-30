// LeetCode 1968 - Array With Elements Not Equal to Average of Neighbors
// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

using System;

public class Solution {
    public int[] RearrangeArray(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length, mid = (n + 1) / 2;
        var ans = new int[n];
        int i = 0, j = mid, k = 0;
        while (i < mid || j < n) {
            if (i < mid) ans[k++] = nums[i++];
            if (j < n) ans[k++] = nums[j++];
        }
        return ans;
    }
}