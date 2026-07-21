// LeetCode 1857 - Largest Color Value in a Directed Graph
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

public class Solution {
    public int LargestPathValue(string colors, int[][] edges) {
        int n = colors.Length;
        var indegree = new int[n];
        var adjacency = new List<int>[n];
        for (int i = 0; i < n; i++) {
            adjacency[i] = new List<int>();
        }
        foreach (var edge in edges) {
            adjacency[edge[0]].Add(edge[1]);
            indegree[edge[1]]++;
        }

        var queue = new Queue<int>();
        for (int node = 0; node < n; node++) {
            if (indegree[node] == 0) {
                queue.Enqueue(node);
            }
        }

        var dp = new int[n][];
        for (int node = 0; node < n; node++) {
            dp[node] = new int[26];
            dp[node][colors[node] - 'a'] = 1;
        }

        int processed = 0;
        int answer = 0;
        while (queue.Count > 0) {
            int node = queue.Dequeue();
            processed++;
            foreach (int value in dp[node]) {
                answer = Math.Max(answer, value);
            }
            foreach (int neighbor in adjacency[node]) {
                int neighborColor = colors[neighbor] - 'a';
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
                    queue.Enqueue(neighbor);
                }
            }
        }
        return processed == n ? answer : -1;
    }
}
