// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/

#include <algorithm>

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
    int heightOfTree(TreeNode* root) {
        if (!root) return -1;
        return dfs(root);
    }

private:
    int dfs(TreeNode* node) {
        if (!node) return -1;
        if (node->left && node->left->right == node) return dfs(node->right) + 1;
        if (node->right && node->right->left == node) return dfs(node->left) + 1;
        return std::max(dfs(node->left), dfs(node->right)) + 1;
    }
};
