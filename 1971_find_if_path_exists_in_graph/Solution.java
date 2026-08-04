// LeetCode 1971 - Find if Path Exists in Graph
// https://leetcode.com/problems/find-if-path-exists-in-graph/

import java.util.*;

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        if (source == destination) return true;
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        boolean[] seen = new boolean[n];
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(source);
        seen[source] = true;
        while (!stack.isEmpty()) {
            int u = stack.pop();
            if (u == destination) return true;
            for (int v : g[u]) {
                if (!seen[v]) {
                    seen[v] = true;
                    stack.push(v);
                }
            }
        }
        return false;
    }
}
