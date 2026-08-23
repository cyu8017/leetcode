// LeetCode 2240 - Number of Ways to Buy Pens and Pencils
// https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

public class Solution {
    public long WaysToBuyPensPencils(int total, int cost1, int cost2) {
        long ans = 0;
        for (int pens = 0; pens * cost1 <= total; pens++) {
            int remain = total - pens * cost1;
            ans += remain / cost2 + 1;
        }
        return ans;
    }
}
