// LeetCode 2110 - Number of Smooth Descent Periods of a Stock
// https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution {
    public long getDescentPeriods(int[] prices) {
        long ans = 1, cur = 1;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] == prices[i - 1] - 1) cur++;
            else cur = 1;
            ans += cur;
        }
        return ans;
    }
}
