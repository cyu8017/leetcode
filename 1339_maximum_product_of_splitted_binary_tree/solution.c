// LeetCode 1339 - Maximum Product of Splitted Binary Tree
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static long long* sums;
static int sumsSize, sumsCap;

static long long total(struct TreeNode* node) {
    if (!node) return 0;
    long long value = node->val + total(node->left) + total(node->right);
    if (sumsSize == sumsCap) {
        sumsCap *= 2;
        sums = (long long*)realloc(sums, sumsCap * sizeof(long long));
    }
    sums[sumsSize++] = value;
    return value;
}

int maxProduct(struct TreeNode* root) {
    sumsCap = 64; sumsSize = 0;
    sums = (long long*)malloc(sumsCap * sizeof(long long));
    long long whole = total(root);
    long long best = 0;
    for (int i = 0; i < sumsSize; i++) {
        long long prod = sums[i] * (whole - sums[i]);
        if (prod > best) best = prod;
    }
    free(sums);
    return (int)(best % 1000000007LL);
}
