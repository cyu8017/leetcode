// LeetCode 0653 - Two Sum IV - Input is a BST
// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

#include <stdbool.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static bool contains(int* seen, int size, int value) {
    for (int i = 0; i < size; i++) {
        if (seen[i] == value) {
            return true;
        }
    }
    return false;
}

static bool dfs(struct TreeNode* node, int k, int* seen, int* size) {
    if (!node) {
        return false;
    }
    if (contains(seen, *size, k - node->val)) {
        return true;
    }
    seen[(*size)++] = node->val;
    return dfs(node->left, k, seen, size) || dfs(node->right, k, seen, size);
}

bool findTarget(struct TreeNode* root, int k) {
    int* seen = (int*)malloc(10000 * sizeof(int));
    int size = 0;
    bool answer = dfs(root, k, seen, &size);
    free(seen);
    return answer;
}
