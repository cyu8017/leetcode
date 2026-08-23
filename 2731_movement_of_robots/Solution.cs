// LeetCode 2731 - Movement of Robots
// https://leetcode.com/problems/movement-of-robots/

using System;

public class Solution {
    public int SumDistance(int[] nums, string s, int d) {
        const int MOD = 1000000007;
        int n = nums.Length;
        long[] pos = new long[n];
        for (int i = 0; i < n; i++)
            pos[i] = nums[i] + (s[i] == 'R' ? d : -d);
        Array.Sort(pos);
        long ans = 0, pref = 0;
        for (int i = 0; i < n; i++) {
            ans = (ans + pos[i] * i - pref) % MOD;
            pref += pos[i];
        }
        return (int)((ans % MOD + MOD) % MOD);
    }
}
