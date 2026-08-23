// LeetCode 2529 - Maximum Count of Positive Integer and Negative Integer
// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

using System;

public class Solution {
    public int MaximumCount(int[] nums) {
        int pos = 0, neg = 0;
        foreach (int x in nums) {
            if (x > 0) pos++;
            else if (x < 0) neg++;
        }
        return Math.Max(pos, neg);
    }
}
