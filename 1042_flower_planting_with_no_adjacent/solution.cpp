// LeetCode 1042 - Flower Planting With No Adjacent
// https://leetcode.com/problems/flower-planting-with-no-adjacent/

#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> gardenNoAdj(int n, std::vector<std::vector<int>>& paths) {
        std::vector<std::vector<int>> graph(n + 1);
        for (auto& p : paths) {
            graph[p[0]].push_back(p[1]);
            graph[p[1]].push_back(p[0]);
        }
        std::vector<int> ans(n + 1, 0);
        for (int garden = 1; garden <= n; ++garden) {
            std::unordered_set<int> used;
            for (int nei : graph[garden]) used.insert(ans[nei]);
            for (int c = 1; c <= 4; ++c) {
                if (!used.count(c)) {
                    ans[garden] = c;
                    break;
                }
            }
        }
        return std::vector<int>(ans.begin() + 1, ans.end());
    }
};

