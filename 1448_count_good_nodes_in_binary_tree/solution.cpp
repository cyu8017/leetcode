struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <algorithm>
#include <climits>

class Solution {
    int visit(TreeNode* node, int maximum) {
        if (!node) return 0;
        int good = node->val >= maximum;
        maximum = std::max(maximum, node->val);
        return good + visit(node->left, maximum) + visit(node->right, maximum);
    }
public:
    int goodNodes(TreeNode* root) {
        return visit(root, INT_MIN);
    }
};
