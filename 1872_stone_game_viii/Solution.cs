// LeetCode 1872 - Stone Game VIII
// https://leetcode.com/problems/stone-game-viii/

public class Solution {
    public int StoneGameVIII(int[] stones) {
        int n = stones.Length;
        for (int i = 1; i < n; i++) {
            stones[i] += stones[i - 1];
        }
        int score = stones[n - 1];
        for (int i = n - 2; i >= 1; i--) {
            score = Math.Max(stones[i] - score, score);
        }
        return score;
    }
}
