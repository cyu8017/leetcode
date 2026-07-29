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
    bool visit(TreeNode* node, const std::vector<int>& arr, int index) {
        if (!node || index == (int)arr.size() || node->val != arr[index]) return false;
        if (!node->left && !node->right) return index == (int)arr.size() - 1;
        return visit(node->left, arr, index + 1) || visit(node->right, arr, index + 1);
    }
public:
    bool isValidSequence(TreeNode* root, std::vector<int>& arr) {
        return visit(root, arr, 0);
    }
};
