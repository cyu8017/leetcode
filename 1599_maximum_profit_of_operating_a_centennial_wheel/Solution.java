// LeetCode 1599 - Maximum Profit of Operating a Centennial Wheel
// https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

class Solution {
    public int minOperationsMaxProfit(int[] customers, int boardingCost, int runningCost) {
        int waiting = 0;
        int profit = 0;
        int best = 0;
        int answer = 0;
        int rotation = 0;
        int i = 0;
        while (i < customers.length || waiting > 0) {
            if (i < customers.length) {
                waiting += customers[i];
            }
            int boarded = Math.min(4, waiting);
            waiting -= boarded;
            rotation++;
            profit += boarded * boardingCost - runningCost;
            if (profit > best) {
                best = profit;
                answer = rotation;
            }
            i++;
        }
        return best > 0 ? answer : -1;
    }
}
