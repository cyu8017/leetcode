// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

using System.Collections.Generic;

public class Solution {
    public int[] CountVisitedNodes(IList<int> edges) {
        int n = edges.Count;
        int[] ans = new int[n], state = new int[n];
        var stack = new List<int>();
        void Dfs(int u) {
            state[u] = 1;
            stack.Add(u);
            int v = edges[u];
            if (state[v] == 0) Dfs(v);
            else if (state[v] == 1) {
                int idx = stack.Count - 1;
                while (stack[idx] != v) idx--;
                int cyc = stack.Count - idx;
                for (int i = idx; i < stack.Count; i++) ans[stack[i]] = cyc;
            }
            if (ans[u] == 0) ans[u] = ans[edges[u]] + 1;
            state[u] = 2;
            stack.RemoveAt(stack.Count - 1);
        }
        for (int i = 0; i < n; i++) if (state[i] == 0) Dfs(i);
        return ans;
    }
}
