// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

#include <utility>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        return dfs(root).first;
    }

private:
    std::pair<TreeNode*, int> dfs(TreeNode* node) {
        if (!node) return {nullptr, 0};
        auto left = dfs(node->left);
        auto right = dfs(node->right);
        if (left.second > right.second) return {left.first, left.second + 1};
        if (right.second > left.second) return {right.first, right.second + 1};
        return {node, left.second + 1};
    }
};
