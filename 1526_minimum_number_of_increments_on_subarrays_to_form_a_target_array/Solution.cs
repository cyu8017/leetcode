// LeetCode 1526 - Minimum Number of Increments on Subarrays to Form a Target Array
// https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

using System;

public class Solution {
    public int MinNumberOperations(int[] target) {
        int ans = target[0];
        for (int i = 1; i < target.Length; i++) {
            ans += Math.Max(0, target[i] - target[i - 1]);
        }
        return ans;
    }
}
