// LeetCode 2331 - Evaluate Boolean Binary Tree
// https://leetcode.com/problems/evaluate-boolean-binary-tree/

#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool evaluateTree(struct TreeNode* root) {
    if (!root->left && !root->right) return root->val == 1;
    bool l = evaluateTree(root->left);
    bool r = evaluateTree(root->right);
    if (root->val == 2) return l || r;
    return l && r;
}
