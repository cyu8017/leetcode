// LeetCode 0285 - Inorder Successor in BST
// https://leetcode.com/problems/inorder-successor-in-bst/

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct TreeNode* inorderSuccessor(struct TreeNode* root, struct TreeNode* p) {
    if (p->right) {
        struct TreeNode* current = p->right;
        while (current->left) {
            current = current->left;
        }
        return current;
    }

    struct TreeNode* successor = NULL;
    struct TreeNode* current = root;
    while (current) {
        if (p->val < current->val) {
            successor = current;
            current = current->left;
        } else {
            current = current->right;
        }
    }
    return successor;
}
