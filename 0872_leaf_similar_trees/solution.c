// LeetCode 0872 - Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/

#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static void collect(struct TreeNode* node, int* out, int* n) {
    if (!node) return;
    if (!node->left && !node->right) { out[(*n)++] = node->val; return; }
    collect(node->left, out, n);
    collect(node->right, out, n);
}

bool leafSimilar(struct TreeNode* root1, struct TreeNode* root2) {
    int a[200], b[200], na = 0, nb = 0;
    collect(root1, a, &na);
    collect(root2, b, &nb);
    if (na != nb) return false;
    for (int i = 0; i < na; i++) if (a[i] != b[i]) return false;
    return true;
}
