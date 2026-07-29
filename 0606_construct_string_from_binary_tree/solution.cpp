// LeetCode 0606 - Construct String from Binary Tree
// https://leetcode.com/problems/construct-string-from-binary-tree/

#include <string>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    std::string tree2str(TreeNode* root) {
        if (!root) {
            return "";
        }
        std::string result = std::to_string(root->val);
        if (root->left || root->right) {
            result += "(" + tree2str(root->left) + ")";
        }
        if (root->right) {
            result += "(" + tree2str(root->right) + ")";
        }
        return result;
    }
};
