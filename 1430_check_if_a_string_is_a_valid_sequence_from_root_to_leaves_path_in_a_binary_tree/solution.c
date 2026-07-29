// LeetCode 1430 - Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
// https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/

#include <stdbool.h>

struct TreeNode { int val; struct TreeNode *left; struct TreeNode *right; };

static bool visit(struct TreeNode* node, int* arr, int arrSize, int index) {
    if (!node || index == arrSize || node->val != arr[index]) return false;
    if (!node->left && !node->right) return index == arrSize - 1;
    return visit(node->left, arr, arrSize, index + 1) || visit(node->right, arr, arrSize, index + 1);
}

bool isValidSequence(struct TreeNode* root, int* arr, int arrSize) {
    return visit(root, arr, arrSize, 0);
}
