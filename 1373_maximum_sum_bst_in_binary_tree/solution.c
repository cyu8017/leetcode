// LeetCode 1373 - Maximum Sum BST in Binary Tree
// https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

#include <limits.h>
#include <stdbool.h>

struct TreeNode { int val; struct TreeNode *left; struct TreeNode *right; };

static int g_ans;
typedef struct { bool ok; int mn, mx, sum; } Info;

static Info dfs(struct TreeNode* node) {
    if (!node) return (Info){true, INT_MAX, INT_MIN, 0};
    Info L = dfs(node->left), R = dfs(node->right);
    if (L.ok && R.ok && L.mx < node->val && node->val < R.mn) {
        int s = L.sum + R.sum + node->val;
        if (s > g_ans) g_ans = s;
        int mn = L.mn < node->val ? L.mn : node->val;
        int mx = R.mx > node->val ? R.mx : node->val;
        return (Info){true, mn, mx, s};
    }
    return (Info){false, 0, 0, 0};
}

int maxSumBST(struct TreeNode* root) {
    g_ans = 0;
    dfs(root);
    return g_ans;
}
