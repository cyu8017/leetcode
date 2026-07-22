// LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static struct TreeNode* dfs(struct TreeNode* node, struct TreeNode* p, struct TreeNode* q, int* found) {
    if (!node) return NULL;
    struct TreeNode* left = dfs(node->left, p, q, found);
    struct TreeNode* right = dfs(node->right, p, q, found);
    if (node == p || node == q) {
        (*found)++;
        return node;
    }
    if (left && right) return node;
    return left ? left : right;
}

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    int found = 0;
    struct TreeNode* ans = dfs(root, p, q, &found);
    return found == 2 ? ans : NULL;
}
