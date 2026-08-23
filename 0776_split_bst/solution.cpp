// LeetCode 0776 - Split BST
// https://leetcode.com/problems/split-bst/

#include <vector>

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
    std::vector<TreeNode*> splitBST(TreeNode* root, int target) {
        if (!root) {
            return {nullptr, nullptr};
        }
        if (root->val <= target) {
            auto parts = splitBST(root->right, target);
            root->right = parts[0];
            return {root, parts[1]};
        }
        auto parts = splitBST(root->left, target);
        root->left = parts[1];
        return {parts[0], root};
    }
};
