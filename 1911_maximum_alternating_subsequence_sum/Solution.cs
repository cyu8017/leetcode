// LeetCode 1911 - Maximum Alternating Subsequence Sum
// https://leetcode.com/problems/maximum-alternating-subsequence-sum/

using System;

public class Solution {
    public long MaxAlternatingSum(int[] nums) {
        long even = 0, odd = 0;
        foreach (int x in nums) {
            long ne = Math.Max(even, odd + x);
            long no = Math.Max(odd, even - x);
            even = ne; odd = no;
        }
        return even;
    }
}