// LeetCode 0783 - Minimum Distance Between BST Nodes
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

#include <limits.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static void dfs(struct TreeNode* node, int* prev, int* best) {
    if (!node) return;
    dfs(node->left, prev, best);
    if (*prev != INT_MIN) {
        int d = node->val - *prev;
        if (d < *best) *best = d;
    }
    *prev = node->val;
    dfs(node->right, prev, best);
}

int minDiffInBST(struct TreeNode* root) {
    int prev = INT_MIN, best = INT_MAX;
    dfs(root, &prev, &best);
    return best;
}
