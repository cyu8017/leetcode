// LeetCode 3238 - Find the Number of Winning Players
// https://leetcode.com/problems/find-the-number-of-winning-players/

using System.Collections.Generic;

public class Solution {
    public int WinningPlayerCount(int n, int[][] pick) {
        int[][] cnt = new int[n][];
        for (int i = 0; i < n; i++) cnt[i] = new int[11];
        var s = new HashSet<int>();
        foreach (var p in pick) {
            int x = p[0], y = p[1];
            cnt[x][y]++;
            if (cnt[x][y] > x) s.Add(x);
        }
        return s.Count;
    }
}
