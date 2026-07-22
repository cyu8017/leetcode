// LeetCode 1602 - Find Nearest Right Node in Binary Tree
// https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct TreeNode* findNearestRightNode(struct TreeNode* root, struct TreeNode* u) {
    if (!root || !u) return NULL;
    struct TreeNode** q = (struct TreeNode**)malloc(100000 * sizeof(struct TreeNode*));
    int front = 0, back = 0;
    q[back++] = root;
    while (front < back) {
        int size = back - front;
        for (int i = 0; i < size; i++) {
            struct TreeNode* node = q[front++];
            if (node == u || node->val == u->val) {
                struct TreeNode* ans = (i + 1 < size) ? q[front] : NULL;
                free(q);
                return ans;
            }
            if (node->left) q[back++] = node->left;
            if (node->right) q[back++] = node->right;
        }
    }
    free(q);
    return NULL;
}
