// LeetCode 1697 - Checking Existence of Edge Length Limited Paths
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

import java.util.Arrays;

class Solution {
    public boolean[] distanceLimitedPathsExist(int n, int[][] edgeList, int[][] queries) {
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        Arrays.sort(edgeList, (a, b) -> Integer.compare(a[2], b[2]));
        Integer[] order = new Integer[queries.length];
        for (int i = 0; i < queries.length; i++) {
            order[i] = i;
        }
        Arrays.sort(order, (i, j) -> Integer.compare(queries[i][2], queries[j][2]));
        boolean[] ans = new boolean[queries.length];
        int i = 0;
        for (int idx : order) {
            int limit = queries[idx][2];
            while (i < edgeList.length && edgeList[i][2] < limit) {
                union(parent, edgeList[i][0], edgeList[i][1]);
                i++;
            }
            ans[idx] = find(parent, queries[idx][0]) == find(parent, queries[idx][1]);
        }
        return ans;
    }

    private int find(int[] parent, int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void union(int[] parent, int a, int b) {
        parent[find(parent, a)] = find(parent, b);
    }
}
