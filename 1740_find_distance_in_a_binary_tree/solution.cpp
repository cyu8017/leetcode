// LeetCode 1740 - Find Distance in a Binary Tree
// https://leetcode.com/problems/find-distance-in-a-binary-tree/

#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int findDistance(TreeNode* root, int p, int q) {
        std::unordered_map<int, std::vector<int>> graph;
        dfs(root, nullptr, graph);
        std::queue<std::pair<int, int>> queue;
        queue.push({p, 0});
        std::unordered_set<int> seen;
        seen.insert(p);
        while (!queue.empty()) {
            auto [node, dist] = queue.front();
            queue.pop();
            if (node == q) {
                return dist;
            }
            for (int nei : graph[node]) {
                if (seen.insert(nei).second) {
                    queue.push({nei, dist + 1});
                }
            }
        }
        return -1;
    }

private:
    void dfs(TreeNode* node, TreeNode* parent, std::unordered_map<int, std::vector<int>>& graph) {
        if (!node) {
            return;
        }
        graph.try_emplace(node->val);
        if (parent) {
            graph[node->val].push_back(parent->val);
            graph[parent->val].push_back(node->val);
        }
        dfs(node->left, node, graph);
        dfs(node->right, node, graph);
    }
};
