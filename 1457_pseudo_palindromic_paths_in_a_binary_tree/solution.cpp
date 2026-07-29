struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    int dfs(TreeNode* node, int mask) {
        if (!node) return 0;
        mask ^= 1 << node->val;
        if (!node->left && !node->right) return (mask & (mask - 1)) == 0;
        return dfs(node->left, mask) + dfs(node->right, mask);
    }
public:
    int pseudoPalindromicPaths(TreeNode* root) {
        return dfs(root, 0);
    }
};
