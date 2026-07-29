// LeetCode 0652 - Find Duplicate Subtrees
// https://leetcode.com/problems/find-duplicate-subtrees/

#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct { char* key; int count; } Entry;

static char* serialize(struct TreeNode* node, Entry* entries, int* entryCount, struct TreeNode** result, int* resultCount) {
    if (!node) return strdup("#");
    char* left = serialize(node->left, entries, entryCount, result, resultCount);
    char* right = serialize(node->right, entries, entryCount, result, resultCount);
    char* key = (char*)malloc(strlen(left) + strlen(right) + 32);
    sprintf(key, "%d,%s,%s", node->val, left, right);
    free(left); free(right);
    int found = -1;
    for (int i = 0; i < *entryCount; i++) if (strcmp(entries[i].key, key) == 0) { found = i; break; }
    if (found < 0) {
        entries[*entryCount].key = strdup(key);
        entries[*entryCount].count = 1;
        (*entryCount)++;
    } else {
        entries[found].count++;
        if (entries[found].count == 2) result[(*resultCount)++] = node;
    }
    return key;
}

struct TreeNode** findDuplicateSubtrees(struct TreeNode* root, int* returnSize) {
    Entry entries[10000];
    int entryCount = 0;
    struct TreeNode** result = (struct TreeNode**)malloc(10000 * sizeof(struct TreeNode*));
    int resultCount = 0;
    char* key = serialize(root, entries, &entryCount, result, &resultCount);
    free(key);
    for (int i = 0; i < entryCount; i++) free(entries[i].key);
    *returnSize = resultCount;
    return result;
}
