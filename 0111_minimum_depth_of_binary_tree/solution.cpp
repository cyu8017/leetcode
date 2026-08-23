// LeetCode 0111 - Minimum Depth of Binary Tree
#include <algorithm>
struct TreeNode { int val; TreeNode *left, *right; };
class Solution { public: int minDepth(TreeNode* root) {
    if (!root) return 0;
    if (!root->left) return 1 + minDepth(root->right);
    if (!root->right) return 1 + minDepth(root->left);
    return 1 + std::min(minDepth(root->left), minDepth(root->right));
} };