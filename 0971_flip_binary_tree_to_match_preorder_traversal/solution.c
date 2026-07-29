// LeetCode 0971 - Flip Binary Tree To Match Preorder Traversal
// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static int idx;
static int* voyage_g;
static int* flips;
static int fn;

static bool dfs(struct TreeNode* node) {
    if (!node) return true;
    if (node->val != voyage_g[idx]) return false;
    idx++;
    if (node->left && node->left->val != voyage_g[idx]) {
        flips[fn++] = node->val;
        return dfs(node->right) && dfs(node->left);
    }
    return dfs(node->left) && dfs(node->right);
}

int* flipMatchVoyage(struct TreeNode* root, int* voyage, int voyageSize, int* returnSize) {
    (void)voyageSize;
    idx = 0; voyage_g = voyage;
    flips = (int*)malloc(100 * sizeof(int));
    fn = 0;
    if (!dfs(root)) {
        int* ans = (int*)malloc(sizeof(int));
        ans[0] = -1;
        *returnSize = 1;
        free(flips);
        return ans;
    }
    *returnSize = fn;
    return flips;
}
