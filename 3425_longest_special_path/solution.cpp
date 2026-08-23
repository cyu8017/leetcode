// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

#include <functional>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> longestSpecialPath(std::vector<std::vector<int>>& edges, std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        int bestLen = 0, bestNodes = 1;
        std::unordered_map<int, int> last;
        std::function<void(int, int, int, int, std::vector<int>&)> dfs =
            [&](int u, int p, int dist, int left, std::vector<int>& path) {
            int prevPos = -1;
            bool seen = last.count(nums[u]);
            if (seen) prevPos = last[nums[u]];
            last[nums[u]] = (int)path.size();
            int newLeft = left;
            if (seen && prevPos >= left) newLeft = prevPos + 1;
            path.push_back(dist);
            int length = dist - path[newLeft];
            int nodes = (int)path.size() - newLeft;
            if (length > bestLen || (length == bestLen && nodes < bestNodes)) {
                bestLen = length;
                bestNodes = nodes;
            }
            for (auto [to, w] : g[u]) {
                if (to == p) continue;
                dfs(to, u, dist + w, newLeft, path);
            }
            path.pop_back();
            if (seen) last[nums[u]] = prevPos;
            else last.erase(nums[u]);
        };
        std::vector<int> path;
        dfs(0, -1, 0, 0, path);
        return {bestLen, bestNodes};
    }
};
