// LeetCode 0783 - Minimum Distance Between BST Nodes
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

#include <algorithm>
#include <climits>

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
    int minDiffInBST(TreeNode* root) {
        hasPrev_ = false;
        best_ = INT_MAX;
        inorder(root);
        return best_;
    }

private:
    bool hasPrev_;
    int prev_;
    int best_;

    void inorder(TreeNode* node) {
        if (!node) {
            return;
        }
        inorder(node->left);
        if (hasPrev_) {
            best_ = std::min(best_, node->val - prev_);
        }
        prev_ = node->val;
        hasPrev_ = true;
        inorder(node->right);
    }
};
