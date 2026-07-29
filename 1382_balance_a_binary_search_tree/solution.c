// LeetCode 1382 - Balance a Binary Search Tree
// https://leetcode.com/problems/balance-a-binary-search-tree/

#include <stdlib.h>

struct TreeNode { int val; struct TreeNode *left; struct TreeNode *right; };

static struct TreeNode** nodes;
static int nsize, ncap;

static void walk(struct TreeNode* x) {
    if (!x) return;
    walk(x->left);
    if (nsize == ncap) { ncap *= 2; nodes = (struct TreeNode**)realloc(nodes, ncap * sizeof(struct TreeNode*)); }
    nodes[nsize++] = x;
    walk(x->right);
}

static struct TreeNode* build(int l, int r) {
    if (l >= r) return NULL;
    int m = (l + r) / 2;
    struct TreeNode* x = nodes[m];
    x->left = build(l, m);
    x->right = build(m + 1, r);
    return x;
}

struct TreeNode* balanceBST(struct TreeNode* root) {
    ncap = 64; nsize = 0;
    nodes = (struct TreeNode**)malloc(ncap * sizeof(struct TreeNode*));
    walk(root);
    struct TreeNode* ans = build(0, nsize);
    free(nodes);
    return ans;
}
