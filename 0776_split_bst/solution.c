// LeetCode 0776 - Split BST
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode** splitBST(struct TreeNode* root, int target, int* returnSize) {
    struct TreeNode** result = (struct TreeNode**)malloc(2 * sizeof(struct TreeNode*));
    *returnSize = 2;
    if (!root) { result[0]=NULL; result[1]=NULL; return result; }
    if (root->val <= target) {
        struct TreeNode** parts = splitBST(root->right, target, returnSize);
        root->right = parts[0];
        result[0] = root; result[1] = parts[1];
        free(parts);
    } else {
        struct TreeNode** parts = splitBST(root->left, target, returnSize);
        root->left = parts[1];
        result[0] = parts[0]; result[1] = root;
        free(parts);
    }
    *returnSize = 2;
    return result;
}
