// LeetCode 1038 - Binary Search Tree to Greater Sum Tree
// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    int total = 0;
    void reverseInorder(TreeNode* node) {
        if (!node) return;
        reverseInorder(node->right);
        total += node->val;
        node->val = total;
        reverseInorder(node->left);
    }

public:
    TreeNode* bstToGst(TreeNode* root) {
        total = 0;
        reverseInorder(root);
        return root;
    }
};

