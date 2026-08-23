// LeetCode 3001 - Minimum Moves to Capture The Queen
// https://leetcode.com/problems/minimum-moves-to-capture-the-queen/

public class Solution {
    public int MinMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
        if (a == e && (c != a || (d - b) * (d - f) > 0)) return 1;
        if (b == f && (d != b || (c - a) * (c - e) > 0)) return 1;
        if (c - e == d - f && (a - e != b - f || (a - c) * (a - e) > 0)) return 1;
        if (c - e == f - d && (a - e != f - b || (a - c) * (a - e) > 0)) return 1;
        return 2;
    }
}
