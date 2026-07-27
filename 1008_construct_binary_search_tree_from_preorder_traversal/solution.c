// LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal
// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

#include <limits.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int idx;

static struct TreeNode* build(int* preorder, int n, int bound) {
    if (idx == n || preorder[idx] > bound) return NULL;
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = preorder[idx++];
    root->left = build(preorder, n, root->val);
    root->right = build(preorder, n, bound);
    return root;
}

struct TreeNode* bstFromPreorder(int* preorder, int preorderSize) {
    idx = 0;
    return build(preorder, preorderSize, INT_MAX);
}
