// LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
// https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

using System.Collections.Generic;

public class Solution {
    public int NumberOfCleanRooms(int[][] room) {
        int m = room.Length, n = room[0].Length;
        int[][] dirs = new int[][] { new[]{0,1}, new[]{1,0}, new[]{0,-1}, new[]{-1,0} };
        var vis = new HashSet<(int, int, int)>();
        var cleaned = new HashSet<(int, int)> { (0, 0) };
        int r = 0, c = 0, d = 0;
        while (vis.Add((r, c, d))) {
            int nr = r + dirs[d][0], nc = c + dirs[d][1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && room[nr][nc] == 0) {
                r = nr; c = nc;
                cleaned.Add((r, c));
            } else d = (d + 1) % 4;
        }
        return cleaned.Count;
    }
}
