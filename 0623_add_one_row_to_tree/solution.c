// LeetCode 0623 - Add One Row to Tree
// https://leetcode.com/problems/add-one-row-to-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static struct TreeNode* newNode(int val, struct TreeNode* left, struct TreeNode* right) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = left;
    node->right = right;
    return node;
}

static void dfs(struct TreeNode* node, int val, int depth, int current) {
    if (!node) {
        return;
    }
    if (current == depth - 1) {
        node->left = newNode(val, node->left, NULL);
        node->right = newNode(val, NULL, node->right);
        return;
    }
    dfs(node->left, val, depth, current + 1);
    dfs(node->right, val, depth, current + 1);
}

struct TreeNode* addOneRow(struct TreeNode* root, int val, int depth) {
    if (depth == 1) {
        return newNode(val, root, NULL);
    }
    dfs(root, val, depth, 1);
    return root;
}
