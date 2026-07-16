// LeetCode 0199 - Binary Tree Right Side View
// https://leetcode.com/problems/binary-tree-right-side-view/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int* rightSideView(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;
    if (!root) {
        return NULL;
    }

    int capacity = 128;
    int *result = malloc(capacity * sizeof(*result));
    struct TreeNode **queue = malloc(capacity * sizeof(*queue));
    int front = 0;
    int back = 0;
    queue[back++] = root;

    while (front < back) {
        const int level_end = back;
        while (front < level_end) {
            struct TreeNode *node = queue[front++];
            if (front == level_end) {
                result[(*returnSize)++] = node->val;
            }
            if (node->left) queue[back++] = node->left;
            if (node->right) queue[back++] = node->right;
        }
    }
    free(queue);
    return result;
}
