// LeetCode 2731 - Movement of Robots
// https://leetcode.com/problems/movement-of-robots/

import java.util.Arrays;

class Solution {
    public int sumDistance(int[] nums, String s, int d) {
        final int MOD = 1_000_000_007;
        int n = nums.length;
        long[] pos = new long[n];
        for (int i = 0; i < n; i++)
            pos[i] = nums[i] + (s.charAt(i) == 'R' ? d : -d);
        Arrays.sort(pos);
        long ans = 0, pref = 0;
        for (int i = 0; i < n; i++) {
            ans = (ans + pos[i] * i - pref) % MOD;
            pref += pos[i];
        }
        return (int) ((ans % MOD + MOD) % MOD);
    }
}
