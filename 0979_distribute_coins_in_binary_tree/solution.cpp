// LeetCode 0979 - Distribute Coins in Binary Tree
// https://leetcode.com/problems/distribute-coins-in-binary-tree/

#include <cstdlib>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int distributeCoins(TreeNode* root) {
        int ans = 0;
        auto dfs = [&](auto&& self, TreeNode* node) -> int {
            if (!node) return 0;
            int left = self(self, node->left);
            int right = self(self, node->right);
            ans += std::abs(left) + std::abs(right);
            return node->val + left + right - 1;
        };
        dfs(dfs, root);
        return ans;
    }
};
