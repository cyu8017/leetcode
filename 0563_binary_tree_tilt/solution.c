// LeetCode 0563 - Binary Tree Tilt
// https://leetcode.com/problems/binary-tree-tilt/

#include <stddef.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int subtreeSum(struct TreeNode* node, int* total) {
    if (node == NULL) {
        return 0;
    }
    int left = subtreeSum(node->left, total);
    int right = subtreeSum(node->right, total);
    int diff = left - right;
    if (diff < 0) {
        diff = -diff;
    }
    *total += diff;
    return node->val + left + right;
}

int findTilt(struct TreeNode* root) {
    int total = 0;
    subtreeSum(root, &total);
    return total;
}
