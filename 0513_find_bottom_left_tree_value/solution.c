// LeetCode 0513 - Find Bottom Left Tree Value
// https://leetcode.com/problems/find-bottom-left-tree-value/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

int findBottomLeftValue(struct TreeNode* root) {
    struct TreeNode** queue = (struct TreeNode**)malloc(10000 * sizeof(struct TreeNode*));
    int front = 0;
    int rear = 0;
    queue[rear++] = root;
    int leftmost = root->val;

    while (front < rear) {
        const int levelSize = rear - front;
        for (int index = 0; index < levelSize; index++) {
            struct TreeNode* node = queue[front++];
            if (index == 0) {
                leftmost = node->val;
            }
            if (node->left) {
                queue[rear++] = node->left;
            }
            if (node->right) {
                queue[rear++] = node->right;
            }
        }
    }

    free(queue);
    return leftmost;
}
