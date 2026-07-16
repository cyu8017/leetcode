// LeetCode 0444 - Sequence Reconstruction
// https://leetcode.com/problems/sequence-reconstruction/

#include <queue>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool sequenceReconstruction(std::vector<int>& nums, std::vector<std::vector<int>>& sequences) {
        std::unordered_map<int, int> indegree;
        std::unordered_map<int, std::unordered_set<int>> graph;
        std::set<std::pair<int, int>> seenEdges;

        for (int value : nums) {
            indegree[value] = 0;
            graph[value] = {};
        }

        for (const auto& sequence : sequences) {
            for (size_t index = 0; index + 1 < sequence.size(); ++index) {
                int left = sequence[index];
                int right = sequence[index + 1];
                if (seenEdges.count({left, right})) {
                    continue;
                }
                seenEdges.insert({left, right});
                if (!graph[left].count(right)) {
                    graph[left].insert(right);
                    ++indegree[right];
                }
            }
        }

        std::queue<int> nodes;
        for (int value : nums) {
            if (indegree[value] == 0) {
                nodes.push(value);
            }
        }

        std::vector<int> order;
        while (!nodes.empty()) {
            if (nodes.size() > 1) {
                return false;
            }
            int node = nodes.front();
            nodes.pop();
            order.push_back(node);
            for (int neighbor : graph[node]) {
                if (--indegree[neighbor] == 0) {
                    nodes.push(neighbor);
                }
            }
        }

        return order == nums;
    }
};
