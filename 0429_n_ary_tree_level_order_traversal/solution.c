// LeetCode 0429 - N-ary Tree Level Order Traversal
// https://leetcode.com/problems/n-ary-tree-level-order-traversal/

#include <stdlib.h>

struct Node {
    int val;
    int numChildren;
    struct Node** children;
};

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** levelOrder(struct Node* root, int* returnSize, int** returnColumnSizes) {
    if (root == NULL) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    struct Node** queue = (struct Node**)malloc(10000 * sizeof(struct Node*));
    int head = 0;
    int tail = 0;
    queue[tail++] = root;

    int** result = (int**)malloc(1000 * sizeof(int*));
    *returnColumnSizes = (int*)malloc(1000 * sizeof(int));
    int levels = 0;

    while (head < tail) {
        int size = tail - head;
        result[levels] = (int*)malloc((size_t)size * sizeof(int));
        (*returnColumnSizes)[levels] = size;
        for (int i = 0; i < size; i++) {
            struct Node* node = queue[head++];
            result[levels][i] = node->val;
            for (int c = 0; c < node->numChildren; c++) {
                queue[tail++] = node->children[c];
            }
        }
        levels++;
    }

    free(queue);
    *returnSize = levels;
    return result;
}
