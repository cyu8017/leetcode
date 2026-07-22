// LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    TreeNode* dfs(TreeNode* node, int p, int q, int& found) {
        if (!node) {
            return nullptr;
        }
        TreeNode* left = dfs(node->left, p, q, found);
        TreeNode* right = dfs(node->right, p, q, found);
        if (node->val == p || node->val == q) {
            ++found;
            return node;
        }
        if (left && right) {
            return node;
        }
        return left ? left : right;
    }

public:
    TreeNode* lowestCommonAncestor(TreeNode* root, int p, int q) {
        int found = 0;
        TreeNode* ans = dfs(root, p, q, found);
        return found == 2 ? ans : nullptr;
    }
};
