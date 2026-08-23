// LeetCode 0803 - Bricks Falling When Hit
// https://leetcode.com/problems/bricks-falling-when-hit/

using System;

public class Solution {
    public int[] HitBricks(int[][] grid, int[][] hits) {
        int m = grid.Length, n = grid[0].Length, roof = m * n;
        int[] parent = new int[roof + 1], size = new int[roof + 1];
        for (int i = 0; i <= roof; i++) { parent[i] = i; size[i] = 1; }

        int Find(int x) {
            while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
            return x;
        }
        void Unite(int a, int b) {
            int ra = Find(a), rb = Find(b);
            if (ra == rb) return;
            parent[ra] = rb;
            size[rb] += size[ra];
        }
        int Idx(int r, int c) => r * n + c;

        int[][] status = new int[m][];
        for (int r = 0; r < m; r++) {
            status[r] = (int[])grid[r].Clone();
        }
        foreach (var hit in hits) status[hit[0]][hit[1]] = 0;

        int[] dr = { -1, 1, 0, 0 }, dc = { 0, 0, -1, 1 };
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (status[r][c] == 0) continue;
                if (r == 0) Unite(Idx(r, c), roof);
                for (int k = 0; k < 4; k++) {
                    int nr = r + dr[k], nc = c + dc[k];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1)
                        Unite(Idx(r, c), Idx(nr, nc));
                }
            }
        }

        int[] answer = new int[hits.Length];
        for (int i = hits.Length - 1; i >= 0; i--) {
            int r = hits[i][0], c = hits[i][1];
            if (grid[r][c] == 0) continue;
            int prev = size[Find(roof)];
            status[r][c] = 1;
            if (r == 0) Unite(Idx(r, c), roof);
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1)
                    Unite(Idx(r, c), Idx(nr, nc));
            }
            int curr = size[Find(roof)];
            answer[i] = Math.Max(0, curr - prev - 1);
        }
        return answer;
    }
}
