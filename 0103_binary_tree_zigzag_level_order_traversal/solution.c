// LeetCode 0103 - Binary Tree Zigzag Level Order Traversal
// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

#include <stdbool.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** zigzagLevelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    if (!root) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    int capacity = 16;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)capacity * sizeof(int));
    *returnSize = 0;

    struct TreeNode** queue = (struct TreeNode**)malloc(1024 * sizeof(struct TreeNode*));
    int front = 0;
    int rear = 0;
    queue[rear++] = root;
    bool leftToRight = true;

    while (front < rear) {
        int size = rear - front;
        int* level = (int*)malloc((size_t)size * sizeof(int));

        for (int i = 0; i < size; i++) {
            struct TreeNode* node = queue[front++];
            level[i] = node->val;
            if (node->left) {
                queue[rear++] = node->left;
            }
            if (node->right) {
                queue[rear++] = node->right;
            }
        }

        if (!leftToRight) {
            for (int i = 0, j = size - 1; i < j; i++, j--) {
                int tmp = level[i];
                level[i] = level[j];
                level[j] = tmp;
            }
        }

        if (*returnSize >= capacity) {
            capacity *= 2;
            result = (int**)realloc(result, (size_t)capacity * sizeof(int*));
            colSizes = (int*)realloc(colSizes, (size_t)capacity * sizeof(int));
        }
        result[*returnSize] = level;
        colSizes[*returnSize] = size;
        (*returnSize)++;
        leftToRight = !leftToRight;
    }

    free(queue);
    *returnColumnSizes = colSizes;
    return result;
}
