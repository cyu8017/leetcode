// LeetCode 1372 - Longest ZigZag Path in a Binary Tree
// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

struct TreeNode { int val; struct TreeNode *left; struct TreeNode *right; };

static int g_ans;
static void dfs(struct TreeNode* node, int* leftLen, int* rightLen) {
    if (!node) { *leftLen = -1; *rightLen = -1; return; }
    int ll, lr, rl, rr;
    dfs(node->left, &ll, &lr);
    dfs(node->right, &rl, &rr);
    int a = lr + 1, b = rl + 1;
    if (a > g_ans) g_ans = a;
    if (b > g_ans) g_ans = b;
    *leftLen = a; *rightLen = b;
}

int longestZigZag(struct TreeNode* root) {
    g_ans = 0;
    int L, R;
    dfs(root, &L, &R);
    return g_ans;
}
