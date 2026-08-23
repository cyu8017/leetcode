// LeetCode 0112 - Path Sum
struct TreeNode { int val; TreeNode *left, *right; };
class Solution { public: bool hasPathSum(TreeNode* root, int targetSum) {
    if (!root) return false;
    if (!root->left && !root->right) return root->val == targetSum;
    return hasPathSum(root->left, targetSum - root->val) ||
           hasPathSum(root->right, targetSum - root->val);
} };