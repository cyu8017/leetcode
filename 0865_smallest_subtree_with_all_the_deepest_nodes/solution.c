// LeetCode 0865 - Smallest Subtree with all the Deepest Nodes
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

#include <stddef.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct { int depth; struct TreeNode* node; } Pair;

static Pair dfs(struct TreeNode* node) {
    if (!node) return (Pair){0, NULL};
    Pair L = dfs(node->left);
    Pair R = dfs(node->right);
    if (L.depth > R.depth) return (Pair){L.depth + 1, L.node};
    if (R.depth > L.depth) return (Pair){R.depth + 1, R.node};
    return (Pair){L.depth + 1, node};
}

struct TreeNode* subtreeWithAllDeepest(struct TreeNode* root) {
    return dfs(root).node;
}
