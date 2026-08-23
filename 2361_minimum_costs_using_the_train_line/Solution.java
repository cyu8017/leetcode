// LeetCode 2361 - Minimum Costs Using the Train Line
// https://leetcode.com/problems/minimum-costs-using-the-train-line/

class Solution {
    public long[] minimumCosts(int[] regular, int[] express, int expressCost) {
        int n = regular.length;
        long[] ans = new long[n];
        long reg = 0, exp = expressCost;
        for (int i = 0; i < n; i++) {
            long nextReg = Math.min(reg + regular[i], exp + express[i]);
            long nextExp = Math.min(reg + regular[i] + expressCost, exp + express[i]);
            reg = nextReg;
            exp = nextExp;
            ans[i] = Math.min(reg, exp);
        }
        return ans;
    }
}
