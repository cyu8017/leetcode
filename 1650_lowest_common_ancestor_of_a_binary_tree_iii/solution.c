// LeetCode 1650 - Lowest Common Ancestor of a Binary Tree III
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

#include <stddef.h>

struct Node {
    int val;
    struct Node* left;
    struct Node* right;
    struct Node* parent;
};

struct Node* lowestCommonAncestor(struct Node* p, struct Node* q) {
    struct Node* a = p;
    struct Node* b = q;
    while (a != b) {
        a = a ? a->parent : q;
        b = b ? b->parent : p;
    }
    return a;
}
