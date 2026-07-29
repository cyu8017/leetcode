// LeetCode 0437 - Path Sum III
// https://leetcode.com/problems/path-sum-iii/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct {
    long long key;
    int value;
    int used;
} PrefixEntry;

static unsigned int hashLL(long long key, int capacity) {
    unsigned long long x = (unsigned long long)key;
    x ^= x >> 33;
    x *= 0xff51afd7ed558ccdULL;
    x ^= x >> 33;
    return (unsigned int)(x % (unsigned int)capacity);
}

static void prefixAdd(PrefixEntry* table, int capacity, long long key, int delta) {
    unsigned int idx = hashLL(key, capacity);
    while (table[idx].used && table[idx].key != key) {
        idx = (idx + 1) % (unsigned int)capacity;
    }
    if (!table[idx].used) {
        table[idx].used = 1;
        table[idx].key = key;
        table[idx].value = 0;
    }
    table[idx].value += delta;
}

static int prefixGet(PrefixEntry* table, int capacity, long long key) {
    unsigned int idx = hashLL(key, capacity);
    while (table[idx].used) {
        if (table[idx].key == key) {
            return table[idx].value;
        }
        idx = (idx + 1) % (unsigned int)capacity;
    }
    return 0;
}

static int dfs(struct TreeNode* node, long long current, int targetSum, PrefixEntry* table, int capacity) {
    if (node == NULL) {
        return 0;
    }
    current += node->val;
    int total = prefixGet(table, capacity, current - targetSum);
    prefixAdd(table, capacity, current, 1);
    total += dfs(node->left, current, targetSum, table, capacity);
    total += dfs(node->right, current, targetSum, table, capacity);
    prefixAdd(table, capacity, current, -1);
    return total;
}

int pathSum(struct TreeNode* root, int targetSum) {
    int capacity = 2003;
    PrefixEntry* table = (PrefixEntry*)calloc((size_t)capacity, sizeof(PrefixEntry));
    prefixAdd(table, capacity, 0, 1);
    int total = dfs(root, 0, targetSum, table, capacity);
    free(table);
    return total;
}
