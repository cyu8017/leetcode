// LeetCode 3189 - Minimum Moves to Get a Peaceful Board
// https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

using System;

public class Solution {
    public int MinMoves(int[][] rooks) {
        int ans = 0;
        Array.Sort(rooks, (a, b) => a[0].CompareTo(b[0]));
        for (int i = 0; i < rooks.Length; i++) ans += Math.Abs(rooks[i][0] - i);
        Array.Sort(rooks, (a, b) => a[1].CompareTo(b[1]));
        for (int j = 0; j < rooks.Length; j++) ans += Math.Abs(rooks[j][1] - j);
        return ans;
    }
}
