// LeetCode 0663 - Equal Tree Partition
// https://leetcode.com/problems/equal-tree-partition/

#include <stdbool.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static int dfs(struct TreeNode* node, int* sums, int* size) {
    if (!node) return 0;
    int total = node->val + dfs(node->left, sums, size) + dfs(node->right, sums, size);
    sums[(*size)++] = total;
    return total;
}

bool checkEqualTree(struct TreeNode* root) {
    int sums[10000];
    int size = 0;
    int total = dfs(root, sums, &size);
    size--;
    if (total % 2 != 0) return false;
    int half = total / 2;
    for (int i = 0; i < size; i++) if (sums[i] == half) return true;
    return false;
}
