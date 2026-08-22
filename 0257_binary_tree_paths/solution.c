// LeetCode 0257 - Binary Tree Paths
// https://leetcode.com/problems/binary-tree-paths/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct {
    char** items;
    int size;
    int capacity;
} PathList;

static void path_list_add(PathList* list, const char* path) {
    if (list->size == list->capacity) {
        list->capacity = list->capacity ? list->capacity * 2 : 8;
        list->items = realloc(list->items, (size_t)list->capacity * sizeof(char*));
    }
    list->items[list->size++] = strdup(path);
}

static void dfs(struct TreeNode* node, int* path, int depth, PathList* list) {
    if (!node) {
        return;
    }
    path[depth] = node->val;
    if (!node->left && !node->right) {
        char buffer[4096];
        int length = snprintf(buffer, sizeof(buffer), "%d", path[0]);
        for (int i = 1; i <= depth; i++) {
            length += snprintf(buffer + length, sizeof(buffer) - (size_t)length, "->%d", path[i]);
        }
        path_list_add(list, buffer);
    } else {
        dfs(node->left, path, depth + 1, list);
        dfs(node->right, path, depth + 1, list);
    }
}

char** binaryTreePaths(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;
    PathList list = { NULL, 0, 0 };
    if (root) {
        int path[128];
        dfs(root, path, 0, &list);
        *returnSize = list.size;
    }
    return list.items;
}
