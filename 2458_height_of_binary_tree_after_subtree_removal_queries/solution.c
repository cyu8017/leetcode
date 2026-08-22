// LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

#define MAXN2458 100005

static int height2458[MAXN2458];
static int level2458[MAXN2458];
static int levelMax2458[MAXN2458][2];
static int levelCnt2458[MAXN2458];
static int maxDepth2458;

static int max2(int a, int b) { return a > b ? a : b; }

static int dfs2458(struct TreeNode* node, int d) {
    if (!node) return -1;
    if (d > maxDepth2458) maxDepth2458 = d;
    level2458[node->val] = d;
    int h = 1 + max2(dfs2458(node->left, d + 1), dfs2458(node->right, d + 1));
    height2458[node->val] = h;
    if (levelCnt2458[d] == 0) {
        levelMax2458[d][0] = h;
        levelCnt2458[d] = 1;
    } else if (h >= levelMax2458[d][0]) {
        levelMax2458[d][1] = levelMax2458[d][0];
        levelMax2458[d][0] = h;
        levelCnt2458[d] = 2;
    } else if (levelCnt2458[d] == 1 || h > levelMax2458[d][1]) {
        levelMax2458[d][1] = h;
        levelCnt2458[d] = 2;
    }
    return h;
}

int* treeQueries(struct TreeNode* root, int* queries, int queriesSize, int* returnSize) {
    memset(levelCnt2458, 0, sizeof(levelCnt2458));
    maxDepth2458 = 0;
    dfs2458(root, 0);
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int q = queries[i];
        int d = level2458[q];
        int h = height2458[q];
        if (levelMax2458[d][0] == h) {
            if (levelCnt2458[d] > 1) ans[i] = d + levelMax2458[d][1];
            else ans[i] = d - 1;
        } else {
            ans[i] = d + levelMax2458[d][0];
        }
    }
    *returnSize = queriesSize;
    return ans;
}
