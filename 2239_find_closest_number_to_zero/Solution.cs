// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

using System;

public class Solution {
    public int FindClosestNumber(int[] nums) {
        int ans = nums[0];
        foreach (int x in nums) {
            if (Math.Abs(x) < Math.Abs(ans) || (Math.Abs(x) == Math.Abs(ans) && x > ans)) ans = x;
        }
        return ans;
    }
}
