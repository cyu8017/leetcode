// LeetCode 1672 - Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/

class Solution {
    public int maximumWealth(int[][] accounts) {
        int best = 0;
        for (int[] row : accounts) {
            int sum = 0;
            for (int v : row) {
                sum += v;
            }
            best = Math.max(best, sum);
        }
        return best;
    }
}
