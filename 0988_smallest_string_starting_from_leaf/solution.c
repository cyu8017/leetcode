#define _POSIX_C_SOURCE 200809L
// LeetCode 0988 - Smallest String Starting From Leaf
// https://leetcode.com/problems/smallest-string-starting-from-leaf/

#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static char best[1200];
static char path[1200];

static void dfs(struct TreeNode* node, int depth) {
    if (!node) return;
    path[depth] = (char)('a' + node->val);
    if (!node->left && !node->right) {
        char cand[1200];
        for (int i = 0; i <= depth; i++) cand[i] = path[depth - i];
        cand[depth + 1] = 0;
        if (best[0] == 0 || strcmp(cand, best) < 0) strcpy(best, cand);
        return;
    }
    dfs(node->left, depth + 1);
    dfs(node->right, depth + 1);
}

char* smallestFromLeaf(struct TreeNode* root) {
    best[0] = 0;
    dfs(root, 0);
    return strdup(best);
}
