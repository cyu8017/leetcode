// LeetCode 0894 - All Possible Full Binary Trees
// https://leetcode.com/problems/all-possible-full-binary-trees/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static struct TreeNode* clone_tree(struct TreeNode* node) {
    if (!node) return NULL;
    struct TreeNode* n = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    n->val = node->val;
    n->left = clone_tree(node->left);
    n->right = clone_tree(node->right);
    return n;
}

struct TreeNode** allPossibleFBT(int n, int* returnSize) {
    if (n % 2 == 0) { *returnSize = 0; return NULL; }
    static struct TreeNode** memo[21];
    static int memoSize[21];
    static int ready[21];
    if (ready[n]) {
        *returnSize = memoSize[n];
        struct TreeNode** out = (struct TreeNode**)malloc((size_t)memoSize[n] * sizeof(struct TreeNode*));
        for (int i = 0; i < memoSize[n]; i++) out[i] = clone_tree(memo[n][i]);
        return out;
    }
    if (n == 1) {
        struct TreeNode* leaf = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        leaf->val = 0; leaf->left = leaf->right = NULL;
        memo[1] = (struct TreeNode**)malloc(sizeof(struct TreeNode*));
        memo[1][0] = leaf;
        memoSize[1] = 1;
        ready[1] = 1;
        *returnSize = 1;
        struct TreeNode** out = (struct TreeNode**)malloc(sizeof(struct TreeNode*));
        out[0] = clone_tree(leaf);
        return out;
    }
    struct TreeNode** res = (struct TreeNode**)malloc(2000 * sizeof(struct TreeNode*));
    int rc = 0;
    for (int left = 1; left < n; left += 2) {
        int right = n - 1 - left;
        int ls = 0, rs = 0;
        struct TreeNode** L = allPossibleFBT(left, &ls);
        struct TreeNode** R = allPossibleFBT(right, &rs);
        for (int i = 0; i < ls; i++) {
            for (int j = 0; j < rs; j++) {
                struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
                root->val = 0;
                root->left = L[i];
                root->right = R[j];
                res[rc++] = root;
            }
        }
        // Note: L/R trees are shared across combinations - for LeetCode return this is typical
        free(L); free(R);
    }
    memo[n] = (struct TreeNode**)malloc((size_t)rc * sizeof(struct TreeNode*));
    for (int i = 0; i < rc; i++) memo[n][i] = res[i];
    memoSize[n] = rc;
    ready[n] = 1;
    *returnSize = rc;
    return res;
}
