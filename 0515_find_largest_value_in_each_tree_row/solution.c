// LeetCode 0515 - Find Largest Value in Each Tree Row
// https://leetcode.com/problems/find-largest-value-in-each-tree-row/

#include <limits.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

int* largestValues(struct TreeNode* root, int* returnSize) {
    if (root == NULL) {
        *returnSize = 0;
        return NULL;
    }

    int capacity = 16;
    int* result = (int*)malloc((size_t)capacity * sizeof(int));
    *returnSize = 0;

    struct TreeNode** queue = (struct TreeNode**)malloc(10000 * sizeof(struct TreeNode*));
    int front = 0;
    int rear = 0;
    queue[rear++] = root;

    while (front < rear) {
        int levelMax = INT_MIN;
        const int levelSize = rear - front;
        for (int index = 0; index < levelSize; index++) {
            struct TreeNode* node = queue[front++];
            if (node->val > levelMax) {
                levelMax = node->val;
            }
            if (node->left) {
                queue[rear++] = node->left;
            }
            if (node->right) {
                queue[rear++] = node->right;
            }
        }

        if (*returnSize >= capacity) {
            capacity *= 2;
            result = (int*)realloc(result, (size_t)capacity * sizeof(int));
        }
        result[*returnSize] = levelMax;
        (*returnSize)++;
    }

    free(queue);
    return result;
}
