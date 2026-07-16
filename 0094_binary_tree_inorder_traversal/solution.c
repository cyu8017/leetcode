// LeetCode 0094 - Binary Tree Inorder Traversal
// https://leetcode.com/problems/binary-tree-inorder-traversal/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static void push_node(struct TreeNode*** stack, int* size, int* capacity, struct TreeNode* node) {
    if (*size >= *capacity) {
        *capacity = (*capacity == 0) ? 16 : (*capacity * 2);
        *stack = (struct TreeNode**)realloc(*stack, (size_t)(*capacity) * sizeof(struct TreeNode*));
    }
    (*stack)[(*size)++] = node;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int capacity = 16;
    int* result = (int*)malloc((size_t)capacity * sizeof(int));
    *returnSize = 0;
    struct TreeNode** stack = NULL;
    int stackSize = 0;
    int stackCapacity = 0;
    struct TreeNode* current = root;
    while (current || stackSize > 0) {
        while (current) {
            push_node(&stack, &stackSize, &stackCapacity, current);
            current = current->left;
        }
        current = stack[--stackSize];
        if (*returnSize >= capacity) {
            capacity *= 2;
            result = (int*)realloc(result, (size_t)capacity * sizeof(int));
        }
        result[(*returnSize)++] = current->val;
        current = current->right;
    }
    free(stack);
    return result;
}
