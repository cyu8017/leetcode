// LeetCode 0106 - Construct Binary Tree from Inorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static int* g_postorder;
static int g_postIndex;
static int* g_index;

static struct TreeNode* build(int left, int right) {
    if (left > right) {
        return NULL;
    }
    int rootVal = g_postorder[g_postIndex--];
    int mid = g_index[rootVal + 3000];
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = rootVal;
    root->right = build(mid + 1, right);
    root->left = build(left, mid - 1);
    return root;
}

struct TreeNode* buildTree(int* inorder, int inorderSize, int* postorder, int postorderSize) {
    g_postorder = postorder;
    g_postIndex = postorderSize - 1;
    g_index = (int*)malloc(6001 * sizeof(int));
    for (int i = 0; i < inorderSize; i++) {
        g_index[inorder[i] + 3000] = i;
    }
    struct TreeNode* root = build(0, inorderSize - 1);
    free(g_index);
    g_index = NULL;
    return root;
}