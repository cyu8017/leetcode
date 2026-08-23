// LeetCode 2952 - Minimum Number of Coins to be Added
// https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

import java.util.Arrays;

class Solution {
    public int minimumAddedCoins(int[] coins, int target) {
        Arrays.sort(coins);
        int ans = 0, reach = 0, i = 0;
        while (reach < target) {
            if (i < coins.length && coins[i] <= reach + 1) {
                reach += coins[i];
                i++;
            } else {
                reach += reach + 1;
                ans++;
            }
        }
        return ans;
    }
}
