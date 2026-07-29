// LeetCode 0671 - Second Minimum Node In a Binary Tree
// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

#include <limits.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static void dfs(struct TreeNode* node, int first, long long* second) {
    if (!node) return;
    if (node->val > first && node->val < *second) *second = node->val;
    else if (node->val == first) {
        dfs(node->left, first, second);
        dfs(node->right, first, second);
    }
}

int findSecondMinimumValue(struct TreeNode* root) {
    long long second = LLONG_MAX;
    dfs(root, root->val, &second);
    return second == LLONG_MAX ? -1 : (int)second;
}
