// LeetCode 1615 - Maximal Network Rank
// https://leetcode.com/problems/maximal-network-rank/

import java.util.*;

class Solution {
    public int maximalNetworkRank(int n, int[][] roads) {
        int[] degree = new int[n];
        Set<Long> edges = new HashSet<>();
        for (int[] road : roads) {
            int a = road[0], b = road[1];
            degree[a]++;
            degree[b]++;
            edges.add(edgeKey(a, b));
        }
        int ans = 0;
        for (int a = 0; a < n; a++) {
            for (int b = a + 1; b < n; b++) {
                int rank = degree[a] + degree[b];
                if (edges.contains(edgeKey(a, b))) rank--;
                ans = Math.max(ans, rank);
            }
        }
        return ans;
    }

    private long edgeKey(int a, int b) {
        int x = Math.min(a, b), y = Math.max(a, b);
        return ((long) x << 32) | y;
    }
}
