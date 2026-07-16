// LeetCode 0098 - Validate Binary Search Tree
// https://leetcode.com/problems/validate-binary-search-tree/

#include <stdbool.h>
#include <limits.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static bool valid(struct TreeNode* node, long long low, long long high) {
    if (!node) {
        return true;
    }
    if (!(low < node->val && node->val < high)) {
        return false;
    }
    return valid(node->left, low, node->val) && valid(node->right, node->val, high);
}

bool isValidBST(struct TreeNode* root) {
    return valid(root, LLONG_MIN, LLONG_MAX);
}
