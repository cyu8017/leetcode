// LeetCode 3222 - Find the Winning Player in Coin Game
// https://leetcode.com/problems/find-the-winning-player-in-coin-game/

using System;

public class Solution {
    public string LosingPlayer(int x, int y) {
        int k = Math.Min(x / 2, y / 8);
        x -= 2 * k;
        y -= 8 * k;
        if (x > 0 && y >= 4) return "Alice";
        return "Bob";
    }
}
