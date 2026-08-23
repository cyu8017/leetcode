// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

using System;

public class Solution {
    public int SumOfPower(int[] nums) {
        const int MOD = 1000000007;
        Array.Sort(nums);
        long ans = 0, s = 0;
        foreach (int x in nums) {
            ans = (ans + (s + x) % MOD * x % MOD * x) % MOD;
            s = (s * 2 + x) % MOD;
        }
        return (int)ans;
    }
}
