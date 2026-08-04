// LeetCode 1908 - Game of Nim
// https://leetcode.com/problems/game-of-nim/

class Solution {
    public boolean nimGame(int[] piles) {
        int x = 0;
        for (int p : piles) x ^= p;
        return x != 0;
    }
}
