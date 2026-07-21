// LeetCode 1884 - Egg Drop With 2 Eggs and N Floors
// https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

public class Solution {
    public int TwoEggDrop(int n) {
        int moves = 0;
        int covered = 0;
        while (covered < n) {
            moves++;
            covered += moves;
        }
        return moves;
    }
}
