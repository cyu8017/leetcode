// LeetCode 0897 - Increasing Order Search Tree
// https://leetcode.com/problems/increasing-order-search-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static struct TreeNode* cur;

static void inorder(struct TreeNode* node) {
    if (!node) return;
    inorder(node->left);
    node->left = NULL;
    cur->right = node;
    cur = node;
    inorder(node->right);
}

struct TreeNode* increasingBST(struct TreeNode* root) {
    struct TreeNode dummy = {0, NULL, NULL};
    cur = &dummy;
    inorder(root);
    return dummy.right;
}
