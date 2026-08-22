// LeetCode 0538 - Convert BST to Greater Tree
// https://leetcode.com/problems/convert-bst-to-greater-tree/

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static void reverse_inorder(struct TreeNode* node, int* running) {
    if (!node) {
        return;
    }
    reverse_inorder(node->right, running);
    *running += node->val;
    node->val = *running;
    reverse_inorder(node->left, running);
}

void convertBST(struct TreeNode* root) {
    int running = 0;
    reverse_inorder(root, &running);
}
