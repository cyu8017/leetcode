// LeetCode 0701 - Insert into a Binary Search Tree
// https://leetcode.com/problems/insert-into-a-binary-search-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct TreeNode* insertIntoBST(struct TreeNode* root, int val) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    if (!root) {
        return node;
    }
    struct TreeNode* cur = root;
    while (1) {
        if (val < cur->val) {
            if (!cur->left) {
                cur->left = node;
                break;
            }
            cur = cur->left;
        } else {
            if (!cur->right) {
                cur->right = node;
                break;
            }
            cur = cur->right;
        }
    }
    return root;
}
