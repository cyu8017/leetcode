// LeetCode 3155 - Maximum Number of Upgradable Servers
// https://leetcode.com/problems/maximum-number-of-upgradable-servers/

using System;

public class Solution {
    public int[] MaxUpgrades(int[] count, int[] upgrade, int[] sell, int[] money) {
        int[] ans = new int[count.Length];
        for (int i = 0; i < count.Length; i++) {
            long cnt = count[i];
            ans[i] = (int)Math.Min(cnt, (cnt * sell[i] + money[i]) / (upgrade[i] + sell[i]));
        }
        return ans;
    }
}
