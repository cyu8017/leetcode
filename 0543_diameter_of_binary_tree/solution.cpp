// LeetCode 0543 - Diameter of Binary Tree
// https://leetcode.com/problems/diameter-of-binary-tree/

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

    int depth(TreeNode* node) {
        if (!node) {
            return 0;
        }
        const int left = depth(node->left);
        const int right = depth(node->right);
        best_ = std::max(best_, left + right);
        return 1 + std::max(left, right);
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        best_ = 0;
        depth(root);
        return best_;
    }
};
