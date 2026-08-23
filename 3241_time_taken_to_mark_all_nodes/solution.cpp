// LeetCode 3241 - Time Taken to Mark All Nodes
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/

#include <algorithm>
#include <functional>
#include <vector>

class Solution {
    struct MarkNode {
        int node = 0;
        int time = 0;
    };
    struct Top2 {
        MarkNode top1;
        MarkNode top2;
    };

public:
    std::vector<int> timeTaken(std::vector<std::vector<int>>& edges) {
        int n = (int)edges.size() + 1;
        std::vector<int> ans(n);
        std::vector<std::vector<int>> tree(n);
        std::vector<Top2> dp(n);
        for (auto& e : edges) {
            tree[e[0]].push_back(e[1]);
            tree[e[1]].push_back(e[0]);
        }
        auto getTime = [](int u) { return u % 2 == 0 ? 2 : 1; };
        std::function<int(int, int)> dfs = [&](int u, int prev) -> int {
            MarkNode t1{}, t2{};
            for (int v : tree[u]) {
                if (v == prev) continue;
                int t = dfs(v, u) + getTime(v);
                if (t >= t1.time) {
                    t2 = t1;
                    t1 = MarkNode{v, t};
                } else if (t > t2.time) {
                    t2 = MarkNode{v, t};
                }
            }
            dp[u] = Top2{t1, t2};
            return t1.time;
        };
        std::function<void(int, int, int)> reroot = [&](int u, int prev, int maxTime) {
            ans[u] = maxTime;
            if (dp[u].top1.time > ans[u]) ans[u] = dp[u].top1.time;
            for (int v : tree[u]) {
                if (v == prev) continue;
                int side = dp[u].top1.time;
                if (dp[u].top1.node == v) side = dp[u].top2.time;
                int newMax = std::max(maxTime, side);
                reroot(v, u, getTime(u) + newMax);
            }
        };
        dfs(0, -1);
        reroot(0, -1, 0);
        return ans;
    }
};
