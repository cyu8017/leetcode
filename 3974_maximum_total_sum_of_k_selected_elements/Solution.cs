// LeetCode 3974 - Maximum Total Sum Of K Selected Elements
// https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

using System;

public class Solution {
    public long MaxSum(int[] nums, int k, int mul) {
        Array.Sort(nums);
        int n = nums.Length;
        long ans = 0;
        for (int i = n - 1; i >= n - k; i--) {
            int m = Math.Max(1, mul);
            ans += (long)nums[i] * m;
            mul--;
        }
        return ans;
    }
}
