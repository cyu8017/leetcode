// LeetCode 0110 - Balanced Binary Tree
// https://leetcode.com/problems/balanced-binary-tree/

#include <cstdlib>
#include <algorithm>

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
    bool isBalanced(TreeNode* root) {
        return height(root) != -1;
    }

private:
    int height(TreeNode* node) {
        if (!node) {
            return 0;
        }
        int left = height(node->left);
        if (left == -1) {
            return -1;
        }
        int right = height(node->right);
        if (right == -1) {
            return -1;
        }
        if (std::abs(left - right) > 1) {
            return -1;
        }
        return 1 + std::max(left, right);
    }
};
