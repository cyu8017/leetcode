// LeetCode 1510 - Stone Game IV
// https://leetcode.com/problems/stone-game-iv/

class Solution {
    public boolean winnerSquareGame(int n) {
        boolean[] win = new boolean[n + 1];
        for (int value = 1; value <= n; value++) {
            for (int root = 1; root * root <= value; root++) {
                if (!win[value - root * root]) {
                    win[value] = true;
                    break;
                }
            }
        }
        return win[n];
    }
}
