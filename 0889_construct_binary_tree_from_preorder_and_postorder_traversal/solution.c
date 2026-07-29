// LeetCode 0889 - Construct Binary Tree from Preorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static int* preorder;
static int* post_index;

static struct TreeNode* build(int pre_lo, int pre_hi, int post_lo, int post_hi) {
    if (pre_lo > pre_hi) return NULL;
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = preorder[pre_lo];
    root->left = root->right = NULL;
    if (pre_lo == pre_hi) return root;
    int left_val = preorder[pre_lo + 1];
    int left_post = post_index[left_val];
    int left_size = left_post - post_lo + 1;
    root->left = build(pre_lo + 1, pre_lo + left_size, post_lo, left_post);
    root->right = build(pre_lo + left_size + 1, pre_hi, left_post + 1, post_hi - 1);
    return root;
}

struct TreeNode* constructFromPrePost(int* preorderArr, int preorderSize, int* postorder, int postorderSize) {
    (void)postorderSize;
    preorder = preorderArr;
    post_index = (int*)malloc(1001 * sizeof(int));
    for (int i = 0; i < preorderSize; i++) post_index[postorder[i]] = i;
    struct TreeNode* root = build(0, preorderSize - 1, 0, preorderSize - 1);
    free(post_index);
    return root;
}
