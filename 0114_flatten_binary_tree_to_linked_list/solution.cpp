// LeetCode 0114 - Flatten Binary Tree to Linked List
struct TreeNode { int val; TreeNode *left, *right; };
class Solution {
    TreeNode* flattenTail(TreeNode* n) {
        if (!n) return nullptr;
        TreeNode *leftTail = flattenTail(n->left), *rightTail = flattenTail(n->right);
        if (leftTail) { leftTail->right = n->right; n->right = n->left; n->left = nullptr; }
        return rightTail ? rightTail : (leftTail ? leftTail : n);
    }
public: void flatten(TreeNode* root) { flattenTail(root); }
};