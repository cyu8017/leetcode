// LeetCode 1530 - Number of Good Leaf Nodes Pairs
// https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int answer1530;

static int* dfs1530(struct TreeNode* node, int distance, int* outSize) {
    if (!node) {
        *outSize = 0;
        return NULL;
    }
    if (!node->left && !node->right) {
        int* res = (int*)malloc(sizeof(int));
        res[0] = 1;
        *outSize = 1;
        return res;
    }
    int ls = 0, rs = 0;
    int* left = dfs1530(node->left, distance, &ls);
    int* right = dfs1530(node->right, distance, &rs);
    for (int i = 0; i < ls; i++) {
        for (int j = 0; j < rs; j++) {
            if (left[i] + right[j] <= distance) answer1530++;
        }
    }
    int* res = (int*)malloc((size_t)(ls + rs) * sizeof(int));
    int sz = 0;
    for (int i = 0; i < ls; i++) if (left[i] + 1 < distance) res[sz++] = left[i] + 1;
    for (int i = 0; i < rs; i++) if (right[i] + 1 < distance) res[sz++] = right[i] + 1;
    free(left);
    free(right);
    *outSize = sz;
    return res;
}

int countPairs(struct TreeNode* root, int distance) {
    answer1530 = 0;
    int sz = 0;
    free(dfs1530(root, distance, &sz));
    return answer1530;
}
