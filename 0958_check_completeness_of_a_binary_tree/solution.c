// LeetCode 0958 - Check Completeness of a Binary Tree
// https://leetcode.com/problems/check-completeness-of-a-binary-tree/

#include <stdbool.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool isCompleteTree(struct TreeNode* root) {
    struct TreeNode** q = (struct TreeNode**)malloc(200 * sizeof(struct TreeNode*));
    int head = 0, tail = 0;
    q[tail++] = root;
    int end = 0;
    while (head < tail) {
        struct TreeNode* node = q[head++];
        if (!node) end = 1;
        else {
            if (end) { free(q); return false; }
            q[tail++] = node->left;
            q[tail++] = node->right;
        }
    }
    free(q);
    return true;
}
