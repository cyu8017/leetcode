// LeetCode 2415 - Reverse Odd Levels of Binary Tree
// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

#include <utility>

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
    TreeNode* reverseOddLevels(TreeNode* root) {
        auto dfs = [&](auto&& self, TreeNode* a, TreeNode* b, int level) -> void {
            if (!a || !b) return;
            if (level % 2 == 1) std::swap(a->val, b->val);
            self(self, a->left, b->right, level + 1);
            self(self, a->right, b->left, level + 1);
        };
        if (root) dfs(dfs, root->left, root->right, 1);
        return root;
    }
};
