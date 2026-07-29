// LeetCode 0965 - Univalued Binary Tree
// https://leetcode.com/problems/univalued-binary-tree/

#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static bool dfs(struct TreeNode* node, int v) {
    if (!node) return true;
    if (node->val != v) return false;
    return dfs(node->left, v) && dfs(node->right, v);
}

bool isUnivalTree(struct TreeNode* root) {
    if (!root) return true;
    return dfs(root, root->val);
}
