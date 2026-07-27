// LeetCode 1022 - Sum of Root To Leaf Binary Numbers
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    int dfs(TreeNode* node, int value) {
        if (!node) return 0;
        value = value * 2 + node->val;
        if (!node->left && !node->right) return value;
        return dfs(node->left, value) + dfs(node->right, value);
    }

public:
    int sumRootToLeaf(TreeNode* root) { return dfs(root, 0); }
};

