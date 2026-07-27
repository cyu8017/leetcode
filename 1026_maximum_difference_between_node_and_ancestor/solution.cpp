// LeetCode 1026 - Maximum Difference Between Node and Ancestor
// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

#include <algorithm>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    int dfs(TreeNode* node, int lo, int hi) {
        if (!node) return hi - lo;
        lo = std::min(lo, node->val);
        hi = std::max(hi, node->val);
        return std::max(dfs(node->left, lo, hi), dfs(node->right, lo, hi));
    }

public:
    int maxAncestorDiff(TreeNode* root) { return dfs(root, root->val, root->val); }
};

