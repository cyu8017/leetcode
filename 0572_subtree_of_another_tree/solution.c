// LeetCode 0572 - Subtree of Another Tree
// https://leetcode.com/problems/subtree-of-another-tree/

#include <stdbool.h>
#include <stddef.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static bool same(struct TreeNode* a, struct TreeNode* b) {
    if (a == NULL || b == NULL) {
        return a == b;
    }
    return a->val == b->val && same(a->left, b->left) && same(a->right, b->right);
}

bool isSubtree(struct TreeNode* root, struct TreeNode* subRoot) {
    if (root == NULL) {
        return false;
    }
    return same(root, subRoot) || isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
}
