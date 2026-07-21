// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

#include <stdlib.h>

typedef struct TrieNode {
    int count;
    struct TrieNode* children[2];
} TrieNode;

static TrieNode* trieNew(void) {
    return (TrieNode*)calloc(1, sizeof(TrieNode));
}

static void trieFreeAll(TrieNode* node) {
    if (!node) return;
    trieFreeAll(node->children[0]);
    trieFreeAll(node->children[1]);
    free(node);
}

static void trieInsert(TrieNode* root, int num, int bit) {
    TrieNode* node = root;
    for (int i = bit; i >= 0; i--) {
        int b = (num >> i) & 1;
        if (!node->children[b]) node->children[b] = trieNew();
        node = node->children[b];
        node->count += 1;
    }
}

static int trieQuery(TrieNode* root, int num, int limit, int bit) {
    if (!root || bit < 0) return 0;
    int numBit = (num >> bit) & 1;
    int limitBit = (limit >> bit) & 1;
    TrieNode* child = root->children[numBit];
    if (limitBit == 1) {
        int result = child ? child->count : 0;
        result += trieQuery(root->children[1 - numBit], num, limit, bit - 1);
        return result;
    }
    return trieQuery(child, num, limit, bit - 1);
}

static int countSmallerThan(int* nums, int numsSize, int limit) {
    if (limit <= 0) return 0;
    TrieNode* root = trieNew();
    int total = 0;
    const int maxBit = 15;
    for (int i = 0; i < numsSize; i++) {
        total += trieQuery(root, nums[i], limit, maxBit);
        trieInsert(root, nums[i], maxBit);
    }
    trieFreeAll(root);
    return total;
}

int countPairs(int* nums, int numsSize, int low, int high) {
    return countSmallerThan(nums, numsSize, high + 1) - countSmallerThan(nums, numsSize, low);
}
