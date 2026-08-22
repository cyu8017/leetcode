// LeetCode 0114 - Flatten Binary Tree to Linked List
struct TreeNode { int val; struct TreeNode *left, *right; };
static struct TreeNode* tail(struct TreeNode* n) {
    if (!n) return 0; struct TreeNode *a=tail(n->left), *b=tail(n->right);
    if (a) { a->right=n->right; n->right=n->left; n->left=0; } return b?b:(a?a:n);
}
void flatten(struct TreeNode* root) { tail(root); }