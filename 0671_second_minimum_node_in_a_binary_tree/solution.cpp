// LeetCode 0671 - Second Minimum Node In a Binary Tree
// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    int ans_ = -1;
    int rootVal_ = 0;

    void dfs(TreeNode* node) {
        if (!node) {
            return;
        }
        if (node->val > rootVal_) {
            if (ans_ == -1 || node->val < ans_) {
                ans_ = node->val;
            }
            return;
        }
        dfs(node->left);
        dfs(node->right);
    }

public:
    int findSecondMinimumValue(TreeNode* root) {
        if (!root) {
            return -1;
        }
        ans_ = -1;
        rootVal_ = root->val;
        dfs(root);
        return ans_;
    }
};
