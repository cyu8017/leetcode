// LeetCode 3831 - Median Of A Binary Search Tree Level
// https://leetcode.com/problems/median-of-a-binary-search-tree-level/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static void dfs3831(struct TreeNode* node, int i, int level, int** nums, int* n, int* cap) {
    if (!node) return;
    dfs3831(node->left, i + 1, level, nums, n, cap);
    if (i == level) {
        if (*n == *cap) {
            *cap = *cap ? *cap * 2 : 8;
            *nums = (int*)realloc(*nums, (size_t)(*cap) * sizeof(int));
        }
        (*nums)[(*n)++] = node->val;
    }
    dfs3831(node->right, i + 1, level, nums, n, cap);
}

int levelMedian(struct TreeNode* root, int level) {
    int* nums = NULL;
    int n = 0, cap = 0;
    dfs3831(root, 0, level, &nums, &n, &cap);
    if (n == 0) { free(nums); return -1; }
    int ans = nums[n / 2];
    free(nums);
    return ans;
}
