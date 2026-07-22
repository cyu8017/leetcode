// LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

#include <unordered_set>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    std::unordered_set<int> targets_;

    TreeNode* dfs(TreeNode* node) {
        if (!node) {
            return nullptr;
        }
        TreeNode* left = dfs(node->left);
        TreeNode* right = dfs(node->right);
        if (targets_.count(node->val) || (left && right)) {
            return node;
        }
        return left ? left : right;
    }

    TreeNode* find(TreeNode* node, int val) {
        if (!node) {
            return nullptr;
        }
        if (node->val == val) {
            return node;
        }
        TreeNode* left = find(node->left, val);
        return left ? left : find(node->right, val);
    }

public:
    TreeNode* lowestCommonAncestor(TreeNode* root, std::vector<TreeNode*>& nodes) {
        targets_.clear();
        for (TreeNode* node : nodes) {
            targets_.insert(node->val);
        }
        return dfs(root);
    }

    // Harness may pass node values as ints.
    TreeNode* lowestCommonAncestor(TreeNode* root, std::vector<int>& nodes) {
        targets_.clear();
        targets_.insert(nodes.begin(), nodes.end());
        return dfs(root);
    }
};
