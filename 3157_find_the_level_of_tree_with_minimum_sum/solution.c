// LeetCode 3157 - Find the Level of Tree with Minimum Sum
// https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

#include <stdlib.h>
#include <limits.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

int minimumLevel(struct TreeNode* root) {
    struct TreeNode** q = malloc(100000 * sizeof(struct TreeNode*));
    int qh = 0, qt = 0;
    q[qt++] = root;
    long long best = LLONG_MAX;
    int ans = 0;
    for (int level = 1; qh < qt; level++) {
        int m = qt - qh;
        long long t = 0;
        for (int i = 0; i < m; i++) {
            struct TreeNode* node = q[qh++];
            t += node->val;
            if (node->left) q[qt++] = node->left;
            if (node->right) q[qt++] = node->right;
        }
        if (t < best) { best = t; ans = level; }
    }
    free(q);
    return ans;
}
