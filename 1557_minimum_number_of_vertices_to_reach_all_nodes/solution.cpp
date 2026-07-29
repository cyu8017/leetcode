// LeetCode 1557 - Minimum Number of Vertices to Reach All Nodes
// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> findSmallestSetOfVertices(int n, std::vector<std::vector<int>>& edges) {
        std::unordered_set<int> incoming;
        for (const auto& edge : edges) {
            incoming.insert(edge[1]);
        }
        std::vector<int> result;
        for (int v = 0; v < n; ++v) {
            if (!incoming.count(v)) {
                result.push_back(v);
            }
        }
        return result;
    }
};
