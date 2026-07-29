// LeetCode 0653 - Two Sum IV - Input is a BST
// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

#include <unordered_set>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    std::unordered_set<int> seen_;
    int k_ = 0;

    bool dfs(TreeNode* node) {
        if (!node) {
            return false;
        }
        if (seen_.count(k_ - node->val)) {
            return true;
        }
        seen_.insert(node->val);
        return dfs(node->left) || dfs(node->right);
    }

public:
    bool findTarget(TreeNode* root, int k) {
        seen_.clear();
        k_ = k;
        return dfs(root);
    }
};
