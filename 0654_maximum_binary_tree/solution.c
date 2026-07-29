// LeetCode 0654 - Maximum Binary Tree
// https://leetcode.com/problems/maximum-binary-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static struct TreeNode* build(int* nums, int left, int right) {
    if (left > right) {
        return NULL;
    }
    int mid = left;
    for (int i = left; i <= right; i++) {
        if (nums[i] > nums[mid]) {
            mid = i;
        }
    }
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = nums[mid];
    node->left = build(nums, left, mid - 1);
    node->right = build(nums, mid + 1, right);
    return node;
}

struct TreeNode* constructMaximumBinaryTree(int* nums, int numsSize) {
    return build(nums, 0, numsSize - 1);
}
