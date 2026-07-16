// LeetCode 0501 - Find Mode in Binary Search Tree
// https://leetcode.com/problems/find-mode-in-binary-search-tree/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct {
    int key;
    int count;
} CountEntry;

static void inorder(struct TreeNode* node, CountEntry* entries, int* entryCount, int* best) {
    if (node == NULL) {
        return;
    }
    inorder(node->left, entries, entryCount, best);
    int index = 0;
    for (; index < *entryCount; index++) {
        if (entries[index].key == node->val) {
            entries[index].count++;
            if (entries[index].count > *best) {
                *best = entries[index].count;
            }
            break;
        }
    }
    if (index == *entryCount) {
        entries[*entryCount].key = node->val;
        entries[*entryCount].count = 1;
        if (*entryCount == 0 || entries[*entryCount].count > *best) {
            *best = entries[*entryCount].count;
        }
        (*entryCount)++;
    }
    inorder(node->right, entries, entryCount, best);
}

int* findMode(struct TreeNode* root, int* returnSize) {
    CountEntry entries[2000];
    int entryCount = 0;
    int best = 0;
    inorder(root, entries, &entryCount, &best);

    int* result = (int*)malloc((size_t)entryCount * sizeof(int));
    int count = 0;
    for (int index = 0; index < entryCount; index++) {
        if (entries[index].count == best) {
            result[count++] = entries[index].key;
        }
    }
    *returnSize = count;
    return result;
}
