// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

import java.util.Arrays;

class Solution {
    public int sumOfPower(int[] nums) {
        final int MOD = 1_000_000_007;
        Arrays.sort(nums);
        long ans = 0, s = 0;
        for (int x : nums) {
            ans = (ans + (s + x) % MOD * x % MOD * x) % MOD;
            s = (s * 2 + x) % MOD;
        }
        return (int) ans;
    }
}
