// LeetCode 1686 - Stone Game VI
// https://leetcode.com/problems/stone-game-vi/

using System;
using System.Linq;

public class Solution {
    public int StoneGameVI(int[] aliceValues, int[] bobValues) {
        int n = aliceValues.Length;
        var order = Enumerable.Range(0, n)
            .OrderByDescending(i => aliceValues[i] + bobValues[i])
            .ToArray();
        int score = 0;
        for (int t = 0; t < n; t++) {
            int i = order[t];
            score += (t % 2 == 0) ? aliceValues[i] : -bobValues[i];
        }
        return score.CompareTo(0);
    }
}
