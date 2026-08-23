// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<int> countVisitedNodes(std::vector<int>& edges) {
        int n = (int)edges.size();
        std::vector<int> ans(n), state(n);
        std::vector<int> stack;
        std::function<void(int)> dfs = [&](int u) {
            state[u] = 1;
            stack.push_back(u);
            int v = edges[u];
            if (state[v] == 0) dfs(v);
            else if (state[v] == 1) {
                int idx = (int)stack.size() - 1;
                while (stack[idx] != v) idx--;
                int cyc = (int)stack.size() - idx;
                for (int i = idx; i < (int)stack.size(); i++) ans[stack[i]] = cyc;
            }
            if (ans[u] == 0) ans[u] = ans[edges[u]] + 1;
            state[u] = 2;
            stack.pop_back();
        };
        for (int i = 0; i < n; i++) if (state[i] == 0) dfs(i);
        return ans;
    }
};
