// LeetCode 0803 - Bricks Falling When Hit
// https://leetcode.com/problems/bricks-falling-when-hit/

class Solution {
    private int[] parent;
    private int[] size;
    private int n;
    private int roof;

    public int[] hitBricks(int[][] grid, int[][] hits) {
        int m = grid.length;
        n = grid[0].length;
        roof = m * n;
        parent = new int[roof + 1];
        size = new int[roof + 1];
        for (int i = 0; i <= roof; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        int[][] status = new int[m][n];
        for (int r = 0; r < m; r++) status[r] = grid[r].clone();
        for (int[] hit : hits) status[hit[0]][hit[1]] = 0;
        int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (status[r][c] == 0) continue;
                if (r == 0) unite(idx(r, c), roof);
                for (int k = 0; k < 4; k++) {
                    int nr = r + dr[k], nc = c + dc[k];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1) {
                        unite(idx(r, c), idx(nr, nc));
                    }
                }
            }
        }
        int[] answer = new int[hits.length];
        for (int i = hits.length - 1; i >= 0; i--) {
            int r = hits[i][0], c = hits[i][1];
            if (grid[r][c] == 0) continue;
            int prev = size[find(roof)];
            status[r][c] = 1;
            if (r == 0) unite(idx(r, c), roof);
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1) {
                    unite(idx(r, c), idx(nr, nc));
                }
            }
            int curr = size[find(roof)];
            answer[i] = Math.max(0, curr - prev - 1);
        }
        return answer;
    }

    private int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void unite(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return;
        parent[ra] = rb;
        size[rb] += size[ra];
    }

    private int idx(int r, int c) {
        return r * n + c;
    }
}
