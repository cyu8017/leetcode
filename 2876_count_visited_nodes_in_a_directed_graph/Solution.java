// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private int[] edges;
    private int[] ans;
    private int[] state;
    private List<Integer> stack;

    public int[] countVisitedNodes(List<Integer> edgesList) {
        int n = edgesList.size();
        edges = new int[n];
        for (int i = 0; i < n; i++) edges[i] = edgesList.get(i);
        ans = new int[n];
        state = new int[n];
        stack = new ArrayList<>();
        for (int i = 0; i < n; i++) if (state[i] == 0) dfs(i);
        return ans;
    }

    private void dfs(int u) {
        state[u] = 1;
        stack.add(u);
        int v = edges[u];
        if (state[v] == 0) dfs(v);
        else if (state[v] == 1) {
            int idx = stack.size() - 1;
            while (stack.get(idx) != v) idx--;
            int cyc = stack.size() - idx;
            for (int i = idx; i < stack.size(); i++) ans[stack.get(i)] = cyc;
        }
        if (ans[u] == 0) ans[u] = ans[edges[u]] + 1;
        state[u] = 2;
        stack.remove(stack.size() - 1);
    }
}
