// LeetCode 3997 - Count Dominant Nodes in a Binary Tree
// https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

#include <limits.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int ans3997;

static int dfs3997(struct TreeNode* node) {
    if (!node) return INT_MIN;
    int l = dfs3997(node->left);
    int r = dfs3997(node->right);
    int mx = node->val;
    if (l > mx) mx = l;
    if (r > mx) mx = r;
    if (mx == node->val) ans3997++;
    return mx;
}

int countDominantNodes(struct TreeNode* root) {
    ans3997 = 0;
    dfs3997(root);
    return ans3997;
}
