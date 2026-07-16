// LeetCode 0547 - Number of Provinces
// https://leetcode.com/problems/number-of-provinces/

class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    union(parent, i, j);
                }
            }
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            if (find(parent, i) == i) {
                count++;
            }
        }
        return count;
    }

    private int find(int[] parent, int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void union(int[] parent, int a, int b) {
        int rootA = find(parent, a);
        int rootB = find(parent, b);
        if (rootA != rootB) {
            parent[rootB] = rootA;
        }
    }
}
