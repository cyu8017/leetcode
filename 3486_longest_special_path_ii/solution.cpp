// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

#include <vector>
#include <unordered_map>

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
        auto dfs = [&](auto&& self, int u, int p, int dist, std::vector<int>& pathVals, std::vector<int>& pathDist) -> void {
            pathVals.push_back(nums[u]);
            pathDist.push_back(dist);
            std::unordered_map<int, int> freq;
            int dups = 0, left = 0;
            for (int right = 0; right < (int)pathVals.size(); right++) {
                if (++freq[pathVals[right]] == 2) dups++;
                while (dups > 1) {
                    if (freq[pathVals[left]] == 2) dups--;
                    freq[pathVals[left]]--;
                    left++;
                }
            }
            int length = dist - pathDist[left];
            int nodes = (int)pathVals.size() - left;
            if (length > bestLen || (length == bestLen && nodes < bestNodes)) {
                bestLen = length;
                bestNodes = nodes;
            }
            for (auto& [to, w] : g[u]) {
                if (to == p) continue;
                self(self, to, u, dist + w, pathVals, pathDist);
            }
            pathVals.pop_back();
            pathDist.pop_back();
        };
        std::vector<int> pathVals, pathDist;
        dfs(dfs, 0, -1, 0, pathVals, pathDist);
        return {bestLen, bestNodes};
    }
};
