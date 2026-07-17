// LeetCode 1857 - Largest Color Value in a Directed Graph
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

class Solution {
    public int largestPathValue(String colors, int[][] edges) {
        int n = colors.length();
        int[] indegree = new int[n];
        List<List<Integer>> adjacency = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjacency.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            adjacency.get(edge[0]).add(edge[1]);
            indegree[edge[1]]++;
        }

        Deque<Integer> queue = new ArrayDeque<>();
        for (int node = 0; node < n; node++) {
            if (indegree[node] == 0) {
                queue.addLast(node);
            }
        }

        int[][] dp = new int[n][26];
        for (int node = 0; node < n; node++) {
            dp[node][colors.charAt(node) - 'a'] = 1;
        }

        int processed = 0;
        int answer = 0;

        while (!queue.isEmpty()) {
            int node = queue.removeFirst();
            processed++;
            for (int count : dp[node]) {
                answer = Math.max(answer, count);
            }

            for (int neighbor : adjacency.get(node)) {
                int neighborColor = colors.charAt(neighbor) - 'a';
                for (int colorIndex = 0; colorIndex < 26; colorIndex++) {
                    int candidate = dp[node][colorIndex];
                    if (colorIndex == neighborColor) {
                        candidate++;
                    }
                    if (candidate > dp[neighbor][colorIndex]) {
                        dp[neighbor][colorIndex] = candidate;
                    }
                }

                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    queue.addLast(neighbor);
                }
            }
        }

        return processed == n ? answer : -1;
    }
}
