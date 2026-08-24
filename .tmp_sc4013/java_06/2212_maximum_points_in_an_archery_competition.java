// LeetCode 2212 - Maximum Points in an Archery Competition
// https://leetcode.com/problems/maximum-points-in-an-archery-competition/

class Solution {
    private int bestScore = -1;
    private int[] best = new int[12];

    private void dfs(int i, int remain, int score, int[] bob, int[] aliceArrows) {
        if (i == 12) {
            if (score > bestScore) {
                bestScore = score;
                best = bob.clone();
                if (remain > 0) best[0] += remain;
            }
            return;
        }
        dfs(i + 1, remain, score, bob, aliceArrows);
        int need = aliceArrows[i] + 1;
        if (remain >= need) {
            bob[i] = need;
            dfs(i + 1, remain - need, score + i, bob, aliceArrows);
            bob[i] = 0;
        }
    }

    public int[] maximumBobPoints(int numArrows, int[] aliceArrows) {
        bestScore = -1;
        best = new int[12];
        dfs(0, numArrows, 0, new int[12], aliceArrows);
        return best;
    }
}
