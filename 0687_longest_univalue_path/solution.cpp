// LeetCode 0687 - Longest Univalue Path
// https://leetcode.com/problems/longest-univalue-path/

#include <algorithm>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    int best_ = 0;

    int dfs(TreeNode* node) {
        if (!node) {
            return 0;
        }
        const int left = dfs(node->left);
        const int right = dfs(node->right);
        const int leftPath =
            node->left && node->left->val == node->val ? left + 1 : 0;
        const int rightPath =
            node->right && node->right->val == node->val ? right + 1 : 0;
        best_ = std::max(best_, leftPath + rightPath);
        return std::max(leftPath, rightPath);
    }

public:
    int longestUnivaluePath(TreeNode* root) {
        best_ = 0;
        dfs(root);
        return best_;
    }
};
