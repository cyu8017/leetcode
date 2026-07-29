// LeetCode 1469 - Find All The Lonely Nodes
// https://leetcode.com/problems/find-all-the-lonely-nodes/

#include <stdlib.h>

struct TreeNode { int val; struct TreeNode *left; struct TreeNode *right; };

static void dfs(struct TreeNode* node, int** ans, int* an, int* cap) {
    if (!node) return;
    if ((node->left && !node->right) || (!node->left && node->right)) {
        if (*an == *cap) { *cap *= 2; *ans = (int*)realloc(*ans, (*cap) * sizeof(int)); }
        (*ans)[(*an)++] = (node->left ? node->left : node->right)->val;
    }
    dfs(node->left, ans, an, cap);
    dfs(node->right, ans, an, cap);
}

int* getLonelyNodes(struct TreeNode* root, int* returnSize) {
    int cap = 16, an = 0;
    int* ans = (int*)malloc(cap * sizeof(int));
    dfs(root, &ans, &an, &cap);
    *returnSize = an;
    return ans;
}
