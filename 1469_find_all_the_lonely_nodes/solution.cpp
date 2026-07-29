struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <vector>

class Solution {
    std::vector<int> ans;
    void dfs(TreeNode* node) {
        if (!node) return;
        if ((bool)node->left ^ (bool)node->right)
            ans.push_back(node->left ? node->left->val : node->right->val);
        dfs(node->left);
        dfs(node->right);
    }
public:
    std::vector<int> getLonelyNodes(TreeNode* root) {
        dfs(root);
        return ans;
    }
};
