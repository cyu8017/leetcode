// LeetCode 0851 - Loud and Rich
// https://leetcode.com/problems/loud-and-rich/

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<int> loudAndRich(std::vector<std::vector<int>>& richer,
                                 std::vector<int>& quiet) {
        int n = static_cast<int>(quiet.size());
        std::vector<std::vector<int>> graph(n);
        for (auto& e : richer) {
            graph[e[1]].push_back(e[0]);
        }
        std::vector<int> ans(n, -1);
        std::function<int(int)> dfs = [&](int person) -> int {
            if (ans[person] != -1) {
                return ans[person];
            }
            int best = person;
            for (int richerPerson : graph[person]) {
                int cand = dfs(richerPerson);
                if (quiet[cand] < quiet[best]) {
                    best = cand;
                }
            }
            return ans[person] = best;
        };
        for (int i = 0; i < n; ++i) {
            dfs(i);
        }
        return ans;
    }
};
