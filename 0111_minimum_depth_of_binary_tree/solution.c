// LeetCode 0111 - Minimum Depth of Binary Tree
struct TreeNode { int val; struct TreeNode *left, *right; };
int minDepth(struct TreeNode* root) {
    if (!root) return 0;
    if (!root->left) return 1 + minDepth(root->right);
    if (!root->right) return 1 + minDepth(root->left);
    int a=minDepth(root->left), b=minDepth(root->right); return 1+(a<b?a:b);
}