// LeetCode 0637 - Average of Levels in Binary Tree
// https://leetcode.com/problems/average-of-levels-in-binary-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

double* averageOfLevels(struct TreeNode* root, int* returnSize) {
    if (!root) {
        *returnSize = 0;
        return NULL;
    }
    struct TreeNode** queue = (struct TreeNode**)malloc(10000 * sizeof(struct TreeNode*));
    double* result = (double*)malloc(10000 * sizeof(double));
    int head = 0, tail = 0, count = 0;
    queue[tail++] = root;
    while (head < tail) {
        int level = tail - head;
        long long total = 0;
        for (int i = 0; i < level; i++) {
            struct TreeNode* node = queue[head++];
            total += node->val;
            if (node->left) {
                queue[tail++] = node->left;
            }
            if (node->right) {
                queue[tail++] = node->right;
            }
        }
        result[count++] = (double)total / level;
    }
    free(queue);
    *returnSize = count;
    return result;
}
