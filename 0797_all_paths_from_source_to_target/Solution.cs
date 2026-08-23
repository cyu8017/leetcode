// LeetCode 0797 - All Paths From Source to Target
// https://leetcode.com/problems/all-paths-from-source-to-target/

using System.Collections.Generic;

public class Solution {
    private int target;
    private IList<IList<int>> answer;

    public IList<IList<int>> AllPathsSourceTarget(int[][] graph) {
        target = graph.Length - 1;
        answer = new List<IList<int>>();
        var path = new List<int> { 0 };
        Dfs(graph, 0, path);
        return answer;
    }

    private void Dfs(int[][] graph, int node, List<int> path) {
        if (node == target) {
            answer.Add(new List<int>(path));
            return;
        }
        foreach (int nei in graph[node]) {
            path.Add(nei);
            Dfs(graph, nei, path);
            path.RemoveAt(path.Count - 1);
        }
    }
}
