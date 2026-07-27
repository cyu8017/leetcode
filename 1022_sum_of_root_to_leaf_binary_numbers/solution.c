// LeetCode 1022 - Sum of Root To Leaf Binary Numbers
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int dfs(struct TreeNode* node, int value) {
    if (!node) return 0;
    value = value * 2 + node->val;
    if (!node->left && !node->right) return value;
    return dfs(node->left, value) + dfs(node->right, value);
}

int sumRootToLeaf(struct TreeNode* root) {
    return dfs(root, 0);
}
