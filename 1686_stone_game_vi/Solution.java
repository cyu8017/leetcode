// LeetCode 1686 - Stone Game VI
// https://leetcode.com/problems/stone-game-vi/

import java.util.Arrays;

class Solution {
    public int stoneGameVI(int[] aliceValues, int[] bobValues) {
        int n = aliceValues.length;
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) {
            order[i] = i;
        }
        Arrays.sort(order, (i, j) -> Integer.compare(aliceValues[j] + bobValues[j], aliceValues[i] + bobValues[i]));
        int score = 0;
        for (int t = 0; t < n; t++) {
            int i = order[t];
            if ((t & 1) == 0) {
                score += aliceValues[i];
            } else {
                score -= bobValues[i];
            }
        }
        return Integer.compare(score, 0);
    }
}
