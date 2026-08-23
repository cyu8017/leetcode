// LeetCode 2219 - Maximum Sum Score of Array
// https://leetcode.com/problems/maximum-sum-score-of-array/

using System;

public class Solution {
    public long MaximumSumScore(int[] nums) {
        long total = 0, pref = 0;
        foreach (int x in nums) total += x;
        long ans = long.MinValue;
        foreach (int x in nums) {
            pref += x;
            ans = Math.Max(ans, Math.Max(pref, total - pref + x));
        }
        return ans;
    }
}
