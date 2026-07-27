// LeetCode 1038 - Binary Search Tree to Greater Sum Tree
// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int total;

static void reverse_inorder(struct TreeNode* node) {
    if (!node) return;
    reverse_inorder(node->right);
    total += node->val;
    node->val = total;
    reverse_inorder(node->left);
}

struct TreeNode* bstToGst(struct TreeNode* root) {
    total = 0;
    reverse_inorder(root);
    return root;
}
