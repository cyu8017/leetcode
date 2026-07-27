// LeetCode 1026 - Maximum Difference Between Node and Ancestor
// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int dfs(struct TreeNode* node, int lo, int hi) {
    if (!node) return hi - lo;
    if (node->val < lo) lo = node->val;
    if (node->val > hi) hi = node->val;
    int L = dfs(node->left, lo, hi);
    int R = dfs(node->right, lo, hi);
    return L > R ? L : R;
}

int maxAncestorDiff(struct TreeNode* root) {
    return dfs(root, root->val, root->val);
}
