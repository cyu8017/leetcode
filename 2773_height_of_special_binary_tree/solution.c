// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int imax(int a, int b) { return a > b ? a : b; }

static int dfs(struct TreeNode* node) {
    if (!node) return -1;
    if (node->left && node->left->right == node) return dfs(node->right) + 1;
    if (node->right && node->right->left == node) return dfs(node->left) + 1;
    return imax(dfs(node->left), dfs(node->right)) + 1;
}

int heightOfTree(struct TreeNode* root) {
    if (!root) return -1;
    return dfs(root);
}
