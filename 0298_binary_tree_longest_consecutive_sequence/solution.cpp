// LeetCode 0298 - Binary Tree Longest Consecutive Sequence
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

#include <algorithm>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    int dfs(TreeNode* node, TreeNode* parent, int length) {
        if (node == nullptr) {
            return 0;
        }

        int current = (parent != nullptr && parent->val + 1 == node->val) ? length + 1 : 1;
        return std::max({current, dfs(node->left, node, current), dfs(node->right, node, current)});
    }

public:
    int longestConsecutive(TreeNode* root) {
        return dfs(root, nullptr, 0);
    }
};
