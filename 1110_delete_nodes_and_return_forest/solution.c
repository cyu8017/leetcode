// LeetCode 1110 - Delete Nodes And Return Forest
// https://leetcode.com/problems/delete-nodes-and-return-forest/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static bool inDelete(int* to_delete, int to_deleteSize, int val) {
    for (int i = 0; i < to_deleteSize; i++) if (to_delete[i] == val) return true;
    return false;
}

static struct TreeNode* dfs(struct TreeNode* node, bool is_root, int* to_delete, int to_deleteSize,
                            struct TreeNode*** forest, int* forestSize, int* forestCap) {
    if (!node) return NULL;
    bool removed = inDelete(to_delete, to_deleteSize, node->val);
    if (is_root && !removed) {
        if (*forestSize >= *forestCap) {
            *forestCap = *forestCap ? *forestCap * 2 : 8;
            *forest = (struct TreeNode**)realloc(*forest, (size_t)(*forestCap) * sizeof(struct TreeNode*));
        }
        (*forest)[(*forestSize)++] = node;
    }
    node->left = dfs(node->left, removed, to_delete, to_deleteSize, forest, forestSize, forestCap);
    node->right = dfs(node->right, removed, to_delete, to_deleteSize, forest, forestSize, forestCap);
    return removed ? NULL : node;
}

struct TreeNode** delNodes(struct TreeNode* root, int* to_delete, int to_deleteSize, int* returnSize) {
    struct TreeNode** forest = NULL;
    int forestSize = 0, forestCap = 0;
    dfs(root, true, to_delete, to_deleteSize, &forest, &forestSize, &forestCap);
    *returnSize = forestSize;
    return forest;
}
