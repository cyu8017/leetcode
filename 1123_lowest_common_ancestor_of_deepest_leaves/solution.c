// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct { struct TreeNode* node; int depth; } Res;

static Res dfs(struct TreeNode* node) {
    if (!node) return (Res){NULL, 0};
    Res L = dfs(node->left);
    Res R = dfs(node->right);
    if (L.depth > R.depth) return (Res){L.node, L.depth + 1};
    if (R.depth > L.depth) return (Res){R.node, R.depth + 1};
    return (Res){node, L.depth + 1};
}

struct TreeNode* lcaDeepestLeaves(struct TreeNode* root) {
    return dfs(root).node;
}
