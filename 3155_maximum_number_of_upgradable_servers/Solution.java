// LeetCode 3155 - Maximum Number of Upgradable Servers
// https://leetcode.com/problems/maximum-number-of-upgradable-servers/

class Solution {
    public int[] maxUpgrades(int[] count, int[] upgrade, int[] sell, int[] money) {
        int[] ans = new int[count.length];
        for (int i = 0; i < count.length; i++) {
            long cnt = count[i];
            ans[i] = (int)Math.min(cnt, (cnt * sell[i] + money[i]) / (upgrade[i] + sell[i]));
        }
        return ans;
    }
}
