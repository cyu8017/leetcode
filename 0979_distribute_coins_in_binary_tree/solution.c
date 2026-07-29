// LeetCode 0979 - Distribute Coins in Binary Tree
// https://leetcode.com/problems/distribute-coins-in-binary-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static int ans;

static int dfs(struct TreeNode* node) {
    if (!node) return 0;
    int left = dfs(node->left), right = dfs(node->right);
    ans += abs(left) + abs(right);
    return node->val + left + right - 1;
}

int distributeCoins(struct TreeNode* root) {
    ans = 0;
    dfs(root);
    return ans;
}
