// LeetCode 1599 - Maximum Profit of Operating a Centennial Wheel
// https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

using System;

public class Solution {
    public int MinOperationsMaxProfit(int[] customers, int boardingCost, int runningCost) {
        int waiting = 0, profit = 0, best = 0, answer = 0, rotation = 0, i = 0;
        while (i < customers.Length || waiting > 0) {
            if (i < customers.Length) waiting += customers[i];
            int boarded = Math.Min(4, waiting);
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
