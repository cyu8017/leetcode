// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

using System;

public class Solution {
    public int[] ReverseSubarrays(int[] nums, int k) {
        int n = nums.Length;
        int m = n / k;
        for (int i = 0; i < n; i += m) {
            Array.Reverse(nums, i, m);
        }
        return nums;
    }
}
