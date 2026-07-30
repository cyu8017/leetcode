// LeetCode 1510 - Stone Game IV
// https://leetcode.com/problems/stone-game-iv/

public class Solution {
    public bool WinnerSquareGame(int n) {
        bool[] win = new bool[n + 1];
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
