// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* replaceValueInTree(struct TreeNode* root) {
    if (!root) return NULL;
    root->val = 0;
    struct TreeNode** q = (struct TreeNode**)malloc(100000 * sizeof(struct TreeNode*));
    int head = 0, tail = 0;
    q[tail++] = root;
    while (head < tail) {
        int sz = tail - head;
        long long levelSum = 0;
        for (int i = 0; i < sz; i++) {
            struct TreeNode* node = q[head + i];
            if (node->left) levelSum += node->left->val;
            if (node->right) levelSum += node->right->val;
        }
        for (int i = 0; i < sz; i++) {
            struct TreeNode* node = q[head++];
            long long cousin = levelSum;
            if (node->left) cousin -= node->left->val;
            if (node->right) cousin -= node->right->val;
            if (node->left) {
                node->left->val = (int)cousin;
                q[tail++] = node->left;
            }
            if (node->right) {
                node->right->val = (int)cousin;
                q[tail++] = node->right;
            }
        }
    }
    free(q);
    return root;
}
