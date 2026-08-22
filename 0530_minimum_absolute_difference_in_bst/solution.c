// LeetCode 0530 - Minimum Absolute Difference in BST
// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

#include <limits.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static void inorder(struct TreeNode* node, int* best, int* previous, int* hasPrevious) {
    if (!node) {
        return;
    }
    inorder(node->left, best, previous, hasPrevious);
    if (*hasPrevious) {
        const int diff = node->val - *previous;
        if (diff < *best) {
            *best = diff;
        }
    }
    *previous = node->val;
    *hasPrevious = 1;
    inorder(node->right, best, previous, hasPrevious);
}

int getMinimumDifference(struct TreeNode* root) {
    int best = INT_MAX;
    int previous = 0;
    int hasPrevious = 0;
    inorder(root, &best, &previous, &hasPrevious);
    return best;
}
