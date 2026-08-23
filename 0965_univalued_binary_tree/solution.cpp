// LeetCode 0965 - Univalued Binary Tree
// https://leetcode.com/problems/univalued-binary-tree/

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
    bool isUnivalTree(TreeNode* root) {
        if (!root) return true;
        int v = root->val;
        auto dfs = [&](auto&& self, TreeNode* node) -> bool {
            if (!node) return true;
            if (node->val != v) return false;
            return self(self, node->left) && self(self, node->right);
        };
        return dfs(dfs, root);
    }
};
