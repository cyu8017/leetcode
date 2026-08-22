// LeetCode 0110 - Balanced Binary Tree
// https://leetcode.com/problems/balanced-binary-tree/

#include <stdbool.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static int height(struct TreeNode* node) {
    if (!node) {
        return 0;
    }
    int left = height(node->left);
    if (left == -1) {
        return -1;
    }
    int right = height(node->right);
    if (right == -1) {
        return -1;
    }
    if (abs(left - right) > 1) {
        return -1;
    }
    return 1 + (left > right ? left : right);
}

bool isBalanced(struct TreeNode* root) {
    return height(root) != -1;
}
