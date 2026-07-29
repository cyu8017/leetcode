// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

#include <stdlib.h>
#include <limits.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

int maxLevelSum(struct TreeNode* root) {
    struct TreeNode** q = (struct TreeNode**)malloc(10000 * sizeof(struct TreeNode*));
    int qs = 0, qe = 0;
    q[qe++] = root;
    int bestSum = INT_MIN, bestLevel = 1, level = 1;
    while (qs < qe) {
        int sz = qe - qs;
        long long total = 0;
        for (int i = 0; i < sz; i++) {
            struct TreeNode* node = q[qs++];
            total += node->val;
            if (node->left) q[qe++] = node->left;
            if (node->right) q[qe++] = node->right;
        }
        if (total > bestSum) { bestSum = (int)total; bestLevel = level; }
        level++;
    }
    free(q);
    return bestLevel;
}
