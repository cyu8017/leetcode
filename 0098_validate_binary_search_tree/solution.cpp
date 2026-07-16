// LeetCode 0098 - Validate Binary Search Tree
// https://leetcode.com/problems/validate-binary-search-tree/

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
    bool isValidBST(TreeNode* root) {
        return valid(root, LLONG_MIN, LLONG_MAX);
    }

private:
    bool valid(TreeNode* node, long long low, long long high) {
        if (!node) {
            return true;
        }
        if (!(low < node->val && node->val < high)) {
            return false;
        }
        return valid(node->left, low, node->val) && valid(node->right, node->val, high);
    }
};
