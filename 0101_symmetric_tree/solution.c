// LeetCode 0101 - Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static bool mirrors(struct TreeNode* left, struct TreeNode* right) {
    if (!left && !right) {
        return true;
    }
    if (!left || !right || left->val != right->val) {
        return false;
    }
    return mirrors(left->left, right->right) && mirrors(left->right, right->left);
}

bool isSymmetric(struct TreeNode* root) {
    if (!root) {
        return true;
    }
    return mirrors(root->left, root->right);
}
