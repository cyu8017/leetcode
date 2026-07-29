// LeetCode 1506 - Find Root of N-Ary Tree
// https://leetcode.com/problems/find-root-of-n-ary-tree/

#include <stdlib.h>

struct Node {
    int val;
    int numChildren;
    struct Node** children;
};

struct Node* findRoot(struct Node** tree, int treeSize) {
    int value = 0;
    for (int i = 0; i < treeSize; i++) {
        value ^= tree[i]->val;
        for (int j = 0; j < tree[i]->numChildren; j++) {
            value ^= tree[i]->children[j]->val;
        }
    }
    for (int i = 0; i < treeSize; i++) {
        if (tree[i]->val == value) return tree[i];
    }
    return NULL;
}
