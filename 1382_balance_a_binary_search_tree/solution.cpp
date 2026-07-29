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
    std::vector<TreeNode*> nodes;
    void walk(TreeNode* x) {
        if (!x) return;
        walk(x->left);
        nodes.push_back(x);
        walk(x->right);
    }
    TreeNode* build(int l, int r) {
        if (l >= r) return nullptr;
        int m = (l + r) / 2;
        TreeNode* x = nodes[m];
        x->left = build(l, m);
        x->right = build(m + 1, r);
        return x;
    }
public:
    TreeNode* balanceBST(TreeNode* root) {
        walk(root);
        return build(0, (int)nodes.size());
    }
};
