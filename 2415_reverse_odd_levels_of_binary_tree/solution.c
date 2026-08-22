// LeetCode 2415 - Reverse Odd Levels of Binary Tree
// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static void dfs(struct TreeNode* a, struct TreeNode* b, int level) {
    if (!a || !b) return;
    if (level % 2 == 1) { int t = a->val; a->val = b->val; b->val = t; }
    dfs(a->left, b->right, level + 1);
    dfs(a->right, b->left, level + 1);
}

struct TreeNode* reverseOddLevels(struct TreeNode* root) {
    if (root) dfs(root->left, root->right, 1);
    return root;
}
