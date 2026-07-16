// LeetCode 0272 - Closest Binary Search Tree Value II
// https://leetcode.com/problems/closest-binary-search-tree-value-ii/

#include <math.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static void inorder(struct TreeNode* node, int* values, int* size) {
    if (!node) {
        return;
    }
    inorder(node->left, values, size);
    values[(*size)++] = node->val;
    inorder(node->right, values, size);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* closestKValues(struct TreeNode* root, double target, int k, int* returnSize) {
    int capacity = 10000;
    int* values = (int*)malloc((size_t)capacity * sizeof(int));
    int size = 0;
    inorder(root, values, &size);

    int lo = 0;
    int hi = size;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if ((double)values[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }

    int left = lo - 1;
    int right = lo;
    int* result = (int*)malloc((size_t)k * sizeof(int));
    int count = 0;
    while (count < k) {
        if (right >= size ||
            (left >= 0 && fabs((double)values[left] - target) <= fabs((double)values[right] - target))) {
            result[count++] = values[left];
            left--;
        } else {
            result[count++] = values[right];
            right++;
        }
    }

    free(values);
    *returnSize = k;
    return result;
}
