// LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal
// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

#include <climits>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    int i = 0;
    TreeNode* build(const std::vector<int>& preorder, long long bound) {
        if (i == static_cast<int>(preorder.size()) || preorder[i] > bound) return nullptr;
        TreeNode* root = new TreeNode(preorder[i++]);
        root->left = build(preorder, root->val);
        root->right = build(preorder, bound);
        return root;
    }

public:
    TreeNode* bstFromPreorder(std::vector<int>& preorder) {
        i = 0;
        return build(preorder, LLONG_MAX);
    }
};

