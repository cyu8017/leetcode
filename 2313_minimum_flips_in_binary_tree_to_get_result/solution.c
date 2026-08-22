// LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
// https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int mini(int a, int b) { return a < b ? a : b; }
static int min3(int a, int b, int c) {
    if (b < a) a = b;
    if (c < a) a = c;
    return a;
}

static void dfs_flips(struct TreeNode* node, int* f, int* t) {
    if (!node->left && !node->right) {
        if (node->val == 0) { *f = 0; *t = 1; }
        else { *f = 1; *t = 0; }
        return;
    }
    if (node->val == 5) {
        int lf, lt;
        dfs_flips(node->left, &lf, &lt);
        *f = lt; *t = lf;
        return;
    }
    int lf, lt, rf, rt;
    dfs_flips(node->left, &lf, &lt);
    dfs_flips(node->right, &rf, &rt);
    switch (node->val) {
        case 2: // OR
            *f = lf + rf;
            *t = min3(lt + rt, lt + rf, lf + rt);
            break;
        case 3: // AND
            *f = min3(lf + rf, lf + rt, lt + rf);
            *t = lt + rt;
            break;
        case 4: // XOR
            *f = mini(lf + rf, lt + rt);
            *t = mini(lf + rt, lt + rf);
            break;
        default:
            *f = *t = 0;
    }
}

int minimumFlips(struct TreeNode* root, bool result) {
    int f, t;
    dfs_flips(root, &f, &t);
    return result ? t : f;
}
