// LeetCode 0270 - Closest Binary Search Tree Value
// https://leetcode.com/problems/closest-binary-search-tree-value/

#include <cmath>

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
    int closestValue(TreeNode* root, double target) {
        int closest = root->val;
        TreeNode* current = root;
        while (current) {
            if (std::abs(closest - target) > std::abs(current->val - target)) {
                closest = current->val;
            }
            if (current->val == target) {
                return current->val;
            }
            current = target < current->val ? current->left : current->right;
        }
        return closest;
    }
};
