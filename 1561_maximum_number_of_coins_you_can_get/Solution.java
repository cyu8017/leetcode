// LeetCode 1561 - Maximum Number of Coins You Can Get
// https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

import java.util.*;

class Solution {
    public int maxCoins(int[] piles) {
        Arrays.sort(piles);
        int sum = 0;
        for (int i = piles.length / 3; i < piles.length; i += 2) {
            sum += piles[i];
        }
        return sum;
    }
}
