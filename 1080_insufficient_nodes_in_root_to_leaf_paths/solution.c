// LeetCode 1080 - Insufficient Nodes in Root to Leaf Paths
// https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

#include <stddef.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static struct TreeNode* dfs(struct TreeNode* node, int pathSum, int limit) {
    if (!node) {
        return NULL;
    }
    pathSum += node->val;
    if (!node->left && !node->right) {
        return pathSum >= limit ? node : NULL;
    }
    node->left = dfs(node->left, pathSum, limit);
    node->right = dfs(node->right, pathSum, limit);
    if (!node->left && !node->right) {
        return NULL;
    }
    return node;
}

struct TreeNode* sufficientSubset(struct TreeNode* root, int limit) {
    return dfs(root, 0, limit);
}
