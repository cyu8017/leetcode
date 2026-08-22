// LeetCode 0107 - Binary Tree Level Order Traversal II
// https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

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
int** levelOrderBottom(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    *returnSize = 0;
    *returnColumnSizes = NULL;
    if (!root) {
        return NULL;
    }

    int capacity = 16;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)capacity * sizeof(int));

    int queueCapacity = 16;
    struct TreeNode** queue = (struct TreeNode**)malloc((size_t)queueCapacity * sizeof(struct TreeNode*));
    int front = 0;
    int rear = 0;
    queue[rear++] = root;

    while (front < rear) {
        int size = rear - front;
        int* level = (int*)malloc((size_t)size * sizeof(int));
        for (int i = 0; i < size; ++i) {
            struct TreeNode* node = queue[front++];
            level[i] = node->val;
            if (node->left) {
                if (rear >= queueCapacity) {
                    queueCapacity *= 2;
                    queue = (struct TreeNode**)realloc(queue, (size_t)queueCapacity * sizeof(struct TreeNode*));
                }
                queue[rear++] = node->left;
            }
            if (node->right) {
                if (rear >= queueCapacity) {
                    queueCapacity *= 2;
                    queue = (struct TreeNode**)realloc(queue, (size_t)queueCapacity * sizeof(struct TreeNode*));
                }
                queue[rear++] = node->right;
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
    }

    free(queue);

    for (int i = 0, j = *returnSize - 1; i < j; ++i, --j) {
        int* tmpRow = result[i];
        result[i] = result[j];
        result[j] = tmpRow;
        int tmpSize = colSizes[i];
        colSizes[i] = colSizes[j];
        colSizes[j] = tmpSize;
    }

    *returnColumnSizes = colSizes;
    return result;
}
