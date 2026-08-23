// LeetCode 0563 - Binary Tree Tilt
// https://leetcode.com/problems/binary-tree-tilt/

#include <cstdlib>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    int subtreeSum(TreeNode* node, int& total) {
        if (node == nullptr) {
            return 0;
        }
        int left = subtreeSum(node->left, total);
        int right = subtreeSum(node->right, total);
        total += std::abs(left - right);
        return node->val + left + right;
    }

public:
    int findTilt(TreeNode* root) {
        int total = 0;
        subtreeSum(root, total);
        return total;
    }
};
