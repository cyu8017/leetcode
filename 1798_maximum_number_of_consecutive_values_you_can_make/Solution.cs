// LeetCode 1798 - Maximum Number of Consecutive Values You Can Make
// https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

public class Solution {
    public int GetMaximumConsecutive(int[] coins) {
        Array.Sort(coins);
        long reach = 0;
        foreach (int coin in coins) {
            if (coin > reach + 1) break;
            reach += coin;
        }
        return (int)(reach + 1);
    }
}
