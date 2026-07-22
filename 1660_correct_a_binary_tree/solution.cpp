// LeetCode 1660 - Correct a Binary Tree
// https://leetcode.com/problems/correct-a-binary-tree/

#include <unordered_set>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    std::unordered_set<TreeNode*> seen_;

    TreeNode* dfs(TreeNode* node) {
        if (!node) {
            return nullptr;
        }
        if (node->right && seen_.count(node->right)) {
            return nullptr;
        }
        seen_.insert(node);
        node->right = dfs(node->right);
        node->left = dfs(node->left);
        return node;
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
    // Harness passes fromNode/toNode ints used to create the invalid right link.
    TreeNode* correctBinaryTree(TreeNode* root, int fromNode = -1, int toNode = -1) {
        seen_.clear();
        if (fromNode != -1 && toNode != -1) {
            TreeNode* from = find(root, fromNode);
            TreeNode* to = find(root, toNode);
            if (from && to) {
                from->right = to;
            }
        }
        return dfs(root);
    }
};
