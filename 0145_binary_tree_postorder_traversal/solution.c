// LeetCode 0145 - Binary Tree Postorder Traversal
// https://leetcode.com/problems/binary-tree-postorder-traversal/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int *postorderTraversal(struct TreeNode *root, int *returnSize) {
    *returnSize = 0;
    if (!root) {
        return NULL;
    }

    int capacity = 128;
    int *values = malloc(capacity * sizeof(*values));
    struct TreeNode **stack = malloc(capacity * sizeof(*stack));
    int top = 0;
    stack[top++] = root;
    while (top) {
        struct TreeNode *node = stack[--top];
        values[(*returnSize)++] = node->val;
        if (node->left) {
            stack[top++] = node->left;
        }
        if (node->right) {
            stack[top++] = node->right;
        }
    }
    for (int left = 0, right = *returnSize - 1; left < right; ++left, --right) {
        int temp = values[left];
        values[left] = values[right];
        values[right] = temp;
    }
    free(stack);
    return values;
}
