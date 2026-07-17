// LeetCode 1719 - Number Of Ways To Reconstruct A Tree
// https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

class Solution {
    public int checkWays(int[][] pairs) {
        final int MAX = 501;
        boolean[][] adj = new boolean[MAX][MAX];
        int[] degree = new int[MAX];
        boolean[] present = new boolean[MAX];
        for (int[] pair : pairs) {
            int a = pair[0];
            int b = pair[1];
            if (!adj[a][b]) {
                adj[a][b] = true;
                adj[b][a] = true;
                degree[a]++;
                degree[b]++;
            }
            present[a] = true;
            present[b] = true;
        }
        int n = 0;
        for (int v = 1; v < MAX; v++) {
            if (present[v]) {
                n++;
            }
        }
        int root = -1;
        for (int v = 1; v < MAX; v++) {
            if (present[v] && degree[v] == n - 1) {
                root = v;
                break;
            }
        }
        if (root == -1) {
            return 0;
        }
        int ans = 1;
        for (int node = 1; node < MAX; node++) {
            if (!present[node] || node == root) {
                continue;
            }
            int parent = -1;
            int parentDegree = n + 1;
            for (int nei = 1; nei < MAX; nei++) {
                if (adj[node][nei] && degree[nei] >= degree[node] && degree[nei] < parentDegree) {
                    parent = nei;
                    parentDegree = degree[nei];
                }
            }
            if (parent == -1) {
                return 0;
            }
            for (int nei = 1; nei < MAX; nei++) {
                if (adj[node][nei] && nei != parent && !adj[parent][nei]) {
                    return 0;
                }
            }
            if (degree[parent] == degree[node]) {
                ans = 2;
            }
        }
        return ans;
    }
}
