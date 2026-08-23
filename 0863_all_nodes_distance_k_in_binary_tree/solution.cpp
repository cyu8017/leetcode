// LeetCode 0863 - All Nodes Distance K in Binary Tree
// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

#include <functional>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    std::vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        std::unordered_map<TreeNode*, std::vector<TreeNode*>> graph;
        std::function<void(TreeNode*, TreeNode*)> build =
            [&](TreeNode* node, TreeNode* parent) {
                if (!node) {
                    return;
                }
                if (parent) {
                    graph[node].push_back(parent);
                    graph[parent].push_back(node);
                }
                build(node->left, node);
                build(node->right, node);
            };
        build(root, nullptr);

        std::queue<std::pair<TreeNode*, int>> queue;
        queue.push({target, 0});
        std::unordered_set<TreeNode*> seen{target};
        std::vector<int> ans;
        while (!queue.empty()) {
            auto [node, dist] = queue.front();
            queue.pop();
            if (dist == k) {
                ans.push_back(node->val);
                continue;
            }
            for (TreeNode* nei : graph[node]) {
                if (!seen.count(nei)) {
                    seen.insert(nei);
                    queue.push({nei, dist + 1});
                }
            }
        }
        return ans;
    }
};
