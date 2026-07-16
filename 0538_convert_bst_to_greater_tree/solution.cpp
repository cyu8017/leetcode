// LeetCode 0538 - Convert BST to Greater Tree
// https://leetcode.com/problems/convert-bst-to-greater-tree/

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    int running_ = 0;

    void reverseInorder(TreeNode* node) {
        if (!node) {
            return;
        }
        reverseInorder(node->right);
        running_ += node->val;
        node->val = running_;
        reverseInorder(node->left);
    }

public:
    void convertBST(TreeNode* root) {
        running_ = 0;
        reverseInorder(root);
    }
};
