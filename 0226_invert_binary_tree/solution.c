// LeetCode 0226 - Invert Binary Tree
// https://leetcode.com/problems/invert-binary-tree/

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* invertTree(struct TreeNode* root) {
    if (!root) {
        return NULL;
    }
    struct TreeNode* left = invertTree(root->left);
    struct TreeNode* right = invertTree(root->right);
    root->left = right;
    root->right = left;
    return root;
}
