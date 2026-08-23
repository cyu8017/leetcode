// LeetCode 3397 - Maximum Number of Distinct Elements After Operations
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

using System;

public class Solution {
    public int MaxDistinctElements(int[] nums, int k) {
        Array.Sort(nums);
        int ans = 0;
        long prev = long.MinValue / 2;
        foreach (int x in nums) {
            long cur = x - k;
            if (cur <= prev) cur = prev + 1;
            if (cur > x + k) continue;
            ans++;
            prev = cur;
        }
        return ans;
    }
}
