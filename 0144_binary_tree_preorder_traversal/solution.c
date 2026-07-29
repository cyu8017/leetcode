// LeetCode 0144 - Binary Tree Preorder Traversal
// https://leetcode.com/problems/binary-tree-preorder-traversal/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int *preorderTraversal(struct TreeNode *root, int *returnSize) {
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
        if (node->right) {
            stack[top++] = node->right;
        }
        if (node->left) {
            stack[top++] = node->left;
        }
    }
    free(stack);
    return values;
}
