// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

using System;

public class Solution {
    public int MovesToMakeZigzag(int[] nums) {
        int Cost(int start) {
            int ans = 0;
            for (int i = start; i < nums.Length; i += 2) {
                int left = i > 0 ? nums[i - 1] : int.MaxValue;
                int right = i + 1 < nums.Length ? nums[i + 1] : int.MaxValue;
                ans += Math.Max(0, nums[i] - Math.Min(left, right) + 1);
            }
            return ans;
        }
        return Math.Min(Cost(0), Cost(1));
    }
}
