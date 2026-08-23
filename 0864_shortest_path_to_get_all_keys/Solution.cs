// LeetCode 0864 - Shortest Path to Get All Keys
// https://leetcode.com/problems/shortest-path-to-get-all-keys/

using System.Collections.Generic;

public class Solution {
    public int ShortestPathAllKeys(string[] grid) {
        int m = grid.Length, n = grid[0].Length, allKeys = 0, sr = 0, sc = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '@') { sr = i; sc = j; }
                else if (grid[i][j] >= 'a' && grid[i][j] <= 'f') allKeys |= 1 << (grid[i][j] - 'a');
            }
        var queue = new Queue<(int r, int c, int mask, int dist)>();
        queue.Enqueue((sr, sc, 0, 0));
        long Encode(int r, int c, int mask) => ((long)r << 20) | ((long)c << 10) | (uint)mask;
        var seen = new HashSet<long> { Encode(sr, sc, 0) };
        int[] dr = { 1, -1, 0, 0 }, dc = { 0, 0, 1, -1 };
        while (queue.Count > 0) {
            var (r, c, mask, dist) = queue.Dequeue();
            if (mask == allKeys) return dist;
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == '#') continue;
                char cell = grid[nr][nc];
                int nmask = mask;
                if (cell >= 'a' && cell <= 'f') nmask |= 1 << (cell - 'a');
                if (cell >= 'A' && cell <= 'F' && (mask & (1 << (cell - 'A'))) == 0) continue;
                long state = Encode(nr, nc, nmask);
                if (seen.Add(state)) queue.Enqueue((nr, nc, nmask, dist + 1));
            }
        }
        return -1;
    }
}
