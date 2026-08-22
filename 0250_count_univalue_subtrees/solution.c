// LeetCode 0250 - Count Univalue Subtrees
// https://leetcode.com/problems/count-univalue-subtrees/

#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static bool dfs(struct TreeNode* node, int* count) {
    if (!node) {
        return true;
    }
    bool leftOk = dfs(node->left, count);
    bool rightOk = dfs(node->right, count);
    if (!leftOk || !rightOk) {
        return false;
    }
    if (node->left && node->left->val != node->val) {
        return false;
    }
    if (node->right && node->right->val != node->val) {
        return false;
    }
    (*count)++;
    return true;
}

int countUnivalSubtrees(struct TreeNode* root) {
    int count = 0;
    dfs(root, &count);
    return count;
}
