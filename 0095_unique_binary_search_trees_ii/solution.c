// LeetCode 0095 - Unique Binary Search Trees II
// https://leetcode.com/problems/unique-binary-search-trees-ii/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeList {
    struct TreeNode** nodes;
    int size;
    int capacity;
};

static void append_tree(struct TreeList* list, struct TreeNode* node) {
    if (list->size >= list->capacity) {
        list->capacity = list->capacity == 0 ? 8 : list->capacity * 2;
        list->nodes = (struct TreeNode**)realloc(list->nodes, (size_t)list->capacity * sizeof(struct TreeNode*));
    }
    list->nodes[list->size++] = node;
}

static struct TreeList build(int start, int end) {
    struct TreeList trees = {NULL, 0, 0};
    if (start > end) {
        append_tree(&trees, NULL);
        return trees;
    }
    for (int rootVal = start; rootVal <= end; ++rootVal) {
        struct TreeList leftTrees = build(start, rootVal - 1);
        struct TreeList rightTrees = build(rootVal + 1, end);
        for (int i = 0; i < leftTrees.size; ++i) {
            for (int j = 0; j < rightTrees.size; ++j) {
                struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
                root->val = rootVal;
                root->left = leftTrees.nodes[i];
                root->right = rightTrees.nodes[j];
                append_tree(&trees, root);
            }
        }
        free(leftTrees.nodes);
        free(rightTrees.nodes);
    }
    return trees;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct TreeNode** generateTrees(int n, int* returnSize) {
    if (n == 0) {
        *returnSize = 0;
        return NULL;
    }
    struct TreeList trees = build(1, n);
    *returnSize = trees.size;
    return trees.nodes;
}
