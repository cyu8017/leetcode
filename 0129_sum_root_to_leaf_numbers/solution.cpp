// LeetCode 0129 - Sum Root to Leaf Numbers
// https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution {
    int dfs(TreeNode* node, int value) {
        if (!node) return 0;
        value = value * 10 + node->val;
        if (!node->left && !node->right) return value;
        return dfs(node->left, value) + dfs(node->right, value);
    }
public:
    int sumNumbers(TreeNode* root) { return dfs(root, 0); }
};