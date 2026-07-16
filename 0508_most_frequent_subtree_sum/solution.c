// LeetCode 0508 - Most Frequent Subtree Sum
// https://leetcode.com/problems/most-frequent-subtree-sum/

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

static int subtreeSum(struct TreeNode* node, CountEntry* entries, int* entryCount) {
    if (node == NULL) {
        return 0;
    }
    const int total =
        node->val + subtreeSum(node->left, entries, entryCount) + subtreeSum(node->right, entries, entryCount);
    int index = 0;
    for (; index < *entryCount; index++) {
        if (entries[index].key == total) {
            entries[index].count++;
            return total;
        }
    }
    entries[*entryCount].key = total;
    entries[*entryCount].count = 1;
    (*entryCount)++;
    return total;
}

static int compareInts(const void* leftPtr, const void* rightPtr) {
    return *(const int*)leftPtr - *(const int*)rightPtr;
}

int* findFrequentTreeSum(struct TreeNode* root, int* returnSize) {
    CountEntry entries[10000];
    int entryCount = 0;
    subtreeSum(root, entries, &entryCount);
    if (entryCount == 0) {
        *returnSize = 0;
        return NULL;
    }

    int best = 0;
    for (int index = 0; index < entryCount; index++) {
        if (entries[index].count > best) {
            best = entries[index].count;
        }
    }

    int* result = (int*)malloc((size_t)entryCount * sizeof(int));
    int count = 0;
    for (int index = 0; index < entryCount; index++) {
        if (entries[index].count == best) {
            result[count++] = entries[index].key;
        }
    }
    qsort(result, (size_t)count, sizeof(int), compareInts);
    *returnSize = count;
    return result;
}
