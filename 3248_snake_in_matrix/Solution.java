// LeetCode 3248 - Snake in Matrix
// https://leetcode.com/problems/snake-in-matrix/

class Solution {
    public int finalPositionOfSnake(int n, String[] commands) {
        int x = 0, y = 0;
        for (String c : commands) {
            switch (c.charAt(0)) {
                case 'U': x--; break;
                case 'D': x++; break;
                case 'L': y--; break;
                case 'R': y++; break;
            }
        }
        return x * n + y;
    }
}
