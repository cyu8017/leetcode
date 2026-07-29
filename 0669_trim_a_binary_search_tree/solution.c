// LeetCode 0669 - Trim a Binary Search Tree
// https://leetcode.com/problems/trim-a-binary-search-tree/

#include <stddef.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* trimBST(struct TreeNode* root, int low, int high) {
    if (!root) return NULL;
    if (root->val < low) return trimBST(root->right, low, high);
    if (root->val > high) return trimBST(root->left, low, high);
    root->left = trimBST(root->left, low, high);
    root->right = trimBST(root->right, low, high);
    return root;
}
