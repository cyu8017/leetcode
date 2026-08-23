// LeetCode 2146 - K Highest Ranked Items Within a Price Range
// https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

import java.util.*;

class Solution {
    public List<List<Integer>> highestRankedKItems(int[][] grid, int[] pricing, int[] start, int k) {
        int m = grid.length, n = grid[0].length;
        int low = pricing[0], high = pricing[1];
        boolean[][] vis = new boolean[m][n];
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {start[0], start[1], 0});
        vis[start[0]][start[1]] = true;
        List<int[]> cands = new ArrayList<>();
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1], d = cur[2];
            if (grid[r][c] >= low && grid[r][c] <= high)
                cands.add(new int[] {d, grid[r][c], r, c});
            for (int[] dir : dirs) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !vis[nr][nc] && grid[nr][nc] != 0) {
                    vis[nr][nc] = true;
                    q.offer(new int[] {nr, nc, d + 1});
                }
            }
        }
        cands.sort((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            if (a[2] != b[2]) return Integer.compare(a[2], b[2]);
            return Integer.compare(a[3], b[3]);
        });
        if (k > cands.size()) k = cands.size();
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < k; i++) ans.add(Arrays.asList(cands.get(i)[2], cands.get(i)[3]));
        return ans;
    }
}
