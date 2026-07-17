// LeetCode 1743 - Restore the Array From Adjacent Pairs
// https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> restoreArray(std::vector<std::vector<int>>& adjacentPairs) {
        std::unordered_map<int, std::vector<int>> graph;
        for (const auto& pair : adjacentPairs) {
            graph[pair[0]].push_back(pair[1]);
            graph[pair[1]].push_back(pair[0]);
        }
        int start = 0;
        for (const auto& pair : adjacentPairs) {
            if (graph[pair[0]].size() == 1) {
                start = pair[0];
                break;
            }
            if (graph[pair[1]].size() == 1) {
                start = pair[1];
                break;
            }
        }
        int n = graph.size();
        std::vector<int> ans;
        ans.reserve(n);
        ans.push_back(start);
        bool hasPrev = false;
        int prev = 0;
        while ((int)ans.size() < n) {
            int cur = ans.back();
            const auto& neighbors = graph[cur];
            int nxt = (!hasPrev || neighbors[0] != prev) ? neighbors[0] : neighbors[1];
            ans.push_back(nxt);
            prev = cur;
            hasPrev = true;
        }
        return ans;
    }
};
