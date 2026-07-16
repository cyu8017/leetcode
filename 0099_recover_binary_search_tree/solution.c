// LeetCode 0099 - Recover Binary Search Tree
// https://leetcode.com/problems/recover-binary-search-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void recoverTree(struct TreeNode* root) {
    struct TreeNode* first = NULL;
    struct TreeNode* second = NULL;
    struct TreeNode* previous = NULL;
    struct TreeNode** stack = NULL;
    int capacity = 0;
    int size = 0;
    struct TreeNode* current = root;

    while (current || size > 0) {
        while (current) {
            if (size == capacity) {
                capacity = capacity == 0 ? 16 : capacity * 2;
                stack = (struct TreeNode**)realloc(stack, (size_t)capacity * sizeof(struct TreeNode*));
            }
            stack[size++] = current;
            current = current->left;
        }
        current = stack[--size];
        if (previous && previous->val > current->val) {
            if (!first) {
                first = previous;
            }
            second = current;
        }
        previous = current;
        current = current->right;
    }

    if (first && second) {
        int temp = first->val;
        first->val = second->val;
        second->val = temp;
    }

    free(stack);
}
