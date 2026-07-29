// LeetCode 1448 - Count Good Nodes in Binary Tree
// https://leetcode.com/problems/count-good-nodes-in-binary-tree/

#include <limits.h>

struct TreeNode { int val; struct TreeNode *left; struct TreeNode *right; };

static int visit(struct TreeNode* node, int maximum) {
    if (!node) return 0;
    int good = node->val >= maximum;
    if (node->val > maximum) maximum = node->val;
    return good + visit(node->left, maximum) + visit(node->right, maximum);
}

int goodNodes(struct TreeNode* root) {
    return visit(root, INT_MIN);
}
