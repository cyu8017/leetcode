// LeetCode 0530 - Minimum Absolute Difference in BST
// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

#include <algorithm>
#include <climits>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    int best_ = INT_MAX;
    int previous_ = INT_MIN;
    bool hasPrevious_ = false;

    void inorder(TreeNode* node) {
        if (!node) {
            return;
        }
        inorder(node->left);
        if (hasPrevious_) {
            best_ = std::min(best_, node->val - previous_);
        }
        previous_ = node->val;
        hasPrevious_ = true;
        inorder(node->right);
    }

public:
    int getMinimumDifference(TreeNode* root) {
        inorder(root);
        return best_;
    }
};
