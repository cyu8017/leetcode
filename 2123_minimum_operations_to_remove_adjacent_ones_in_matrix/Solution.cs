// LeetCode 2123 - Minimum Operations to Remove Adjacent Ones in Matrix
// https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/

public class Solution {
    public int MinimumOperations(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int[][] id = new int[m][];
        for (int i = 0; i < m; i++) {
            id[i] = new int[n];
            Array.Fill(id[i], -1);
        }
        int cnt = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 1) id[i][j] = cnt++;
        var g = new List<int>[cnt];
        for (int i = 0; i < cnt; i++) g[i] = new List<int>();
        int[][] dirs = { new[]{0,1}, new[]{1,0}, new[]{0,-1}, new[]{-1,0} };
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 1 || (i + j) % 2 != 0) continue;
                int u = id[i][j];
                foreach (var d in dirs) {
                    int ni = i + d[0], nj = j + d[1];
                    if (ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1)
                        g[u].Add(id[ni][nj]);
                }
            }
        }
        int[] match = new int[cnt];
        Array.Fill(match, -1);
        bool Dfs(int u, bool[] seen) {
            foreach (int v in g[u]) {
                if (seen[v]) continue;
                seen[v] = true;
                if (match[v] == -1 || Dfs(match[v], seen)) {
                    match[v] = u;
                    return true;
                }
            }
            return false;
        }
        int ans = 0;
        for (int u = 0; u < cnt; u++) {
            bool ok = false;
            for (int i = 0; i < m && !ok; i++)
                for (int j = 0; j < n; j++)
                    if (id[i][j] == u && (i + j) % 2 == 0) { ok = true; break; }
            if (!ok) continue;
            bool[] seen = new bool[cnt];
            if (Dfs(u, seen)) ans++;
        }
        return ans;
    }
}
