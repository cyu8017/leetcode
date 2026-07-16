// LeetCode 0547 - Number of Provinces
// https://leetcode.com/problems/number-of-provinces/

public class Solution {
    public int FindCircleNum(int[][] isConnected) {
        int n = isConnected.Length;
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    Union(parent, i, j);
                }
            }
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            if (Find(parent, i) == i) {
                count++;
            }
        }
        return count;
    }

    private int Find(int[] parent, int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void Union(int[] parent, int a, int b) {
        int rootA = Find(parent, a);
        int rootB = Find(parent, b);
        if (rootA != rootB) {
            parent[rootB] = rootA;
        }
    }
}
