// LeetCode 0687 - Longest Univalue Path
// https://leetcode.com/problems/longest-univalue-path/

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static int maxInt(int a, int b) { return a > b ? a : b; }

static int dfs(struct TreeNode* node, int* best) {
    if (!node) return 0;
    int left = dfs(node->left, best);
    int right = dfs(node->right, best);
    int leftPath = 0, rightPath = 0;
    if (node->left && node->left->val == node->val) leftPath = left + 1;
    if (node->right && node->right->val == node->val) rightPath = right + 1;
    *best = maxInt(*best, leftPath + rightPath);
    return maxInt(leftPath, rightPath);
}

int longestUnivaluePath(struct TreeNode* root) {
    int best = 0;
    dfs(root, &best);
    return best;
}
