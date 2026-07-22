// LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

#include <stdbool.h>
#include <stddef.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static bool isTarget(struct TreeNode* node, struct TreeNode** nodes, int nodesSize) {
    for (int i = 0; i < nodesSize; i++) if (nodes[i] == node) return true;
    return false;
}

static struct TreeNode* dfs(struct TreeNode* node, struct TreeNode** nodes, int nodesSize) {
    if (!node) return NULL;
    struct TreeNode* L = dfs(node->left, nodes, nodesSize);
    struct TreeNode* R = dfs(node->right, nodes, nodesSize);
    if (isTarget(node, nodes, nodesSize) || (L && R)) return node;
    return L ? L : R;
}

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode** nodes, int nodesSize) {
    return dfs(root, nodes, nodesSize);
}
