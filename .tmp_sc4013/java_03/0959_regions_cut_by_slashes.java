// LeetCode 0959 - Regions Cut By Slashes
// https://leetcode.com/problems/regions-cut-by-slashes/

class Solution {
    private int[] parent;

    public int regionsBySlashes(String[] grid) {
        int n = grid.length;
        parent = new int[n * n * 4];
        for (int i = 0; i < parent.length; i++) parent[i] = i;
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                int root = 4 * (r * n + c);
                char ch = grid[r].charAt(c);
                if (ch == '/') {
                    unite(root + 0, root + 3);
                    unite(root + 1, root + 2);
                } else if (ch == '\\') {
                    unite(root + 0, root + 1);
                    unite(root + 2, root + 3);
                } else {
                    unite(root + 0, root + 1);
                    unite(root + 1, root + 2);
                    unite(root + 2, root + 3);
                }
                if (r + 1 < n) unite(root + 2, root + 4 * n + 0);
                if (c + 1 < n) unite(root + 1, root + 4 + 3);
            }
        }
        int ans = 0;
        for (int i = 0; i < parent.length; i++) if (find(i) == i) ans++;
        return ans;
    }

    private int find(int x) {
        return parent[x] == x ? x : (parent[x] = find(parent[x]));
    }

    private void unite(int a, int b) {
        parent[find(a)] = find(b);
    }
}
