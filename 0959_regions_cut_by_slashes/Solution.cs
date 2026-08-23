// LeetCode 0959 - Regions Cut By Slashes
// https://leetcode.com/problems/regions-cut-by-slashes/

public class Solution {
    public int RegionsBySlashes(string[] grid) {
        int n = grid.Length;
        int[] parent = new int[n * n * 4];
        for (int i = 0; i < parent.Length; i++) parent[i] = i;
        int Find(int x) => parent[x] == x ? x : parent[x] = Find(parent[x]);
        void Unite(int a, int b) { parent[Find(a)] = Find(b); }
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                int root = 4 * (r * n + c);
                char ch = grid[r][c];
                if (ch == '/') {
                    Unite(root + 0, root + 3);
                    Unite(root + 1, root + 2);
                } else if (ch == '\\') {
                    Unite(root + 0, root + 1);
                    Unite(root + 2, root + 3);
                } else {
                    Unite(root + 0, root + 1);
                    Unite(root + 1, root + 2);
                    Unite(root + 2, root + 3);
                }
                if (r + 1 < n) Unite(root + 2, root + 4 * n + 0);
                if (c + 1 < n) Unite(root + 1, root + 4 + 3);
            }
        }
        int ans = 0;
        for (int i = 0; i < parent.Length; i++) if (Find(i) == i) ans++;
        return ans;
    }
}
