// LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static int* g_preorder;
static int g_preIndex;
static int* g_index;

static struct TreeNode* build(int left, int right) {
    if (left > right) {
        return NULL;
    }
    int rootVal = g_preorder[g_preIndex++];
    int mid = g_index[rootVal + 3000];
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = rootVal;
    root->left = build(left, mid - 1);
    root->right = build(mid + 1, right);
    return root;
}

struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize) {
    (void)preorderSize;
    g_preorder = preorder;
    g_preIndex = 0;
    g_index = (int*)malloc(6001 * sizeof(int));
    for (int i = 0; i < inorderSize; i++) {
        g_index[inorder[i] + 3000] = i;
    }
    struct TreeNode* root = build(0, inorderSize - 1);
    free(g_index);
    g_index = NULL;
    return root;
}