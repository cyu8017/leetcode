// LeetCode 0421 - Maximum XOR of Two Numbers in an Array
// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

#include <stdlib.h>
#include <string.h>

typedef struct TrieNode {
    struct TrieNode* children[2];
} TrieNode;

static TrieNode* newTrieNode(void) {
    TrieNode* node = (TrieNode*)calloc(1, sizeof(TrieNode));
    return node;
}

static void freeTrie(TrieNode* node) {
    if (node == NULL) {
        return;
    }
    freeTrie(node->children[0]);
    freeTrie(node->children[1]);
    free(node);
}

int findMaximumXOR(int* nums, int numsSize) {
    int maximum = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > maximum) {
            maximum = nums[i];
        }
    }
    int maxBit = 0;
    while ((1 << maxBit) <= maximum && maxBit < 31) {
        maxBit++;
    }

    TrieNode* root = newTrieNode();
    for (int i = 0; i < numsSize; i++) {
        TrieNode* node = root;
        for (int bit = maxBit - 1; bit >= 0; bit--) {
            int current = (nums[i] >> bit) & 1;
            if (node->children[current] == NULL) {
                node->children[current] = newTrieNode();
            }
            node = node->children[current];
        }
    }

    int best = 0;
    for (int i = 0; i < numsSize; i++) {
        TrieNode* node = root;
        int candidate = 0;
        for (int bit = maxBit - 1; bit >= 0; bit--) {
            int current = (nums[i] >> bit) & 1;
            int target = 1 - current;
            if (node->children[target]) {
                candidate |= 1 << bit;
                node = node->children[target];
            } else {
                node = node->children[current];
            }
        }
        if (candidate > best) {
            best = candidate;
        }
    }

    freeTrie(root);
    return best;
}
