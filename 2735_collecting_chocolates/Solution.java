// LeetCode 2735 - Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/

class Solution {
    public long minCost(int[] nums, int x) {
        int n = nums.length;
        int[] best = (int[])nums.clone();
        long ans = 0;
        for (int v : nums) ans += v;
        for (int rot = 1; rot < n; rot++) {
            long cur = 1L * rot * x;
            for (int i = 0; i < n; i++) {
                best[i] = Math.min(best[i], nums[(i + rot) % n]);
                cur += best[i];
            }
            ans = Math.min(ans, cur);
        }
        return ans;
    }
}
