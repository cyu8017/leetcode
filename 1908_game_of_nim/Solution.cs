// LeetCode 1908 - Game of Nim
// https://leetcode.com/problems/game-of-nim/

public class Solution {
    public bool NimGame(int[] piles) {
        int x = 0;
        foreach (int p in piles) x ^= p;
        return x != 0;
    }
}