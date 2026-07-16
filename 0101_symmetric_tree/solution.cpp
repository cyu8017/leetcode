// LeetCode 0101 - Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

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
    bool isSymmetric(TreeNode* root) {
        if (!root) {
            return true;
        }
        return mirrors(root->left, root->right);
    }

private:
    bool mirrors(TreeNode* left, TreeNode* right) {
        if (!left && !right) {
            return true;
        }
        if (!left || !right || left->val != right->val) {
            return false;
        }
        return mirrors(left->left, right->right) && mirrors(left->right, right->left);
    }
};
