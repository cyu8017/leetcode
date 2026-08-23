// LeetCode 0897 - Increasing Order Search Tree
// https://leetcode.com/problems/increasing-order-search-tree/

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* increasingBST(TreeNode* root) {
        TreeNode dummy(0);
        TreeNode* cur = &dummy;
        auto inorder = [&](auto&& self, TreeNode* node) -> void {
            if (!node) {
                return;
            }
            self(self, node->left);
            node->left = nullptr;
            cur->right = node;
            cur = node;
            self(self, node->right);
        };
        inorder(inorder, root);
        return dummy.right;
    }
};
