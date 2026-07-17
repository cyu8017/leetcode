// LeetCode 1798 - Maximum Number of Consecutive Values You Can Make
// https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

import java.util.Arrays;

class Solution {
    public int getMaximumConsecutive(int[] coins) {
        Arrays.sort(coins);
        long reach = 0;
        for (int coin : coins) {
            if (coin > reach + 1) break;
            reach += coin;
        }
        return (int) (reach + 1);
    }
}
