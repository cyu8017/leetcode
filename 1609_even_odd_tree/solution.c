// LeetCode 1609 - Even Odd Tree
// https://leetcode.com/problems/even-odd-tree/

#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

bool isEvenOddTree(struct TreeNode* root) {
    if (!root) return true;
    struct TreeNode** q = (struct TreeNode**)malloc(100000 * sizeof(struct TreeNode*));
    int front = 0, back = 0, level = 0;
    q[back++] = root;
    while (front < back) {
        int size = back - front;
        int prev = (level % 2 == 0) ? INT_MIN : INT_MAX;
        for (int i = 0; i < size; i++) {
            struct TreeNode* node = q[front++];
            if (node->val % 2 == level % 2) { free(q); return false; }
            if (level % 2 == 0 && node->val <= prev) { free(q); return false; }
            if (level % 2 == 1 && node->val >= prev) { free(q); return false; }
            prev = node->val;
            if (node->left) q[back++] = node->left;
            if (node->right) q[back++] = node->right;
        }
        level++;
    }
    free(q);
    return true;
}
