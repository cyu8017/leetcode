// LeetCode 3248 - Snake in Matrix
// https://leetcode.com/problems/snake-in-matrix/

public class Solution {
    public int FinalPositionOfSnake(int n, string[] commands) {
        int x = 0, y = 0;
        foreach (var c in commands) {
            switch (c[0]) {
                case 'U': x--; break;
                case 'D': x++; break;
                case 'L': y--; break;
                case 'R': y++; break;
            }
        }
        return x * n + y;
    }
}
