// LeetCode 2576 - Find the Maximum Number of Marked Indices
// https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

using System;

public class Solution {
    public int MaxNumOfMarkedIndices(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        int i = 0, ans = 0;
        for (int j = (n + 1) / 2; j < n; ++j) {
            if (2 * nums[i] <= nums[j]) {
                ans += 2;
                i++;
            }
        }
        return ans;
    }
}
