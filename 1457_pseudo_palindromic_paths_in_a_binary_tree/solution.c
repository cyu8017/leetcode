// LeetCode 1457 - Pseudo-Palindromic Paths in a Binary Tree
// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

struct TreeNode { int val; struct TreeNode *left; struct TreeNode *right; };

static int dfs(struct TreeNode* node, int mask) {
    if (!node) return 0;
    mask ^= 1 << node->val;
    if (!node->left && !node->right) return (mask & (mask - 1)) == 0;
    return dfs(node->left, mask) + dfs(node->right, mask);
}

int pseudoPalindromicPaths (struct TreeNode* root) {
    return dfs(root, 0);
}
