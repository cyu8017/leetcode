// LeetCode 0797 - All Paths From Source to Target
// https://leetcode.com/problems/all-paths-from-source-to-target/

import java.util.*;

class Solution {
    private int target;
    private List<List<Integer>> answer;

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        target = graph.length - 1;
        answer = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        path.add(0);
        dfs(graph, 0, path);
        return answer;
    }

    private void dfs(int[][] graph, int node, List<Integer> path) {
        if (node == target) {
            answer.add(new ArrayList<>(path));
            return;
        }
        for (int nei : graph[node]) {
            path.add(nei);
            dfs(graph, nei, path);
            path.remove(path.size() - 1);
        }
    }
}
