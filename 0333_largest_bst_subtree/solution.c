// LeetCode 0333 - Largest BST Subtree
// https://leetcode.com/problems/largest-bst-subtree/

#include <limits.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct {
    int valid;
    int minValue;
    int maxValue;
    int size;
} DfsResult;

static DfsResult dfs(struct TreeNode* node, int* best) {
    if (node == NULL) {
        DfsResult result = {1, INT_MAX, INT_MIN, 0};
        return result;
    }

    DfsResult left = dfs(node->left, best);
    DfsResult right = dfs(node->right, best);

    if (left.valid && right.valid && left.maxValue < node->val && node->val < right.minValue) {
        DfsResult result;
        result.valid = 1;
        result.size = left.size + right.size + 1;
        result.minValue = node->val < left.minValue ? node->val : left.minValue;
        result.maxValue = node->val > right.maxValue ? node->val : right.maxValue;
        if (result.size > *best) {
            *best = result.size;
        }
        return result;
    }

    DfsResult invalid = {0, 0, 0, 0};
    return invalid;
}

int largestBSTSubtree(struct TreeNode* root) {
    int best = 0;
    dfs(root, &best);
    return best;
}
