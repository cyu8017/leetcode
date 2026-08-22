// LeetCode 0173 - Binary Search Tree Iterator
// https://leetcode.com/problems/binary-search-tree-iterator/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    struct TreeNode** stack;
    int size;
    int capacity;
} BSTIterator;

static void pushLeft(BSTIterator* obj, struct TreeNode* node) {
    while (node) {
        if (obj->size == obj->capacity) {
            obj->capacity *= 2;
            obj->stack = realloc(obj->stack, obj->capacity * sizeof(*obj->stack));
        }
        obj->stack[obj->size++] = node;
        node = node->left;
    }
}

BSTIterator* bSTIteratorCreate(struct TreeNode* root) {
    BSTIterator* obj = malloc(sizeof(*obj));
    obj->capacity = 16;
    obj->size = 0;
    obj->stack = malloc(obj->capacity * sizeof(*obj->stack));
    pushLeft(obj, root);
    return obj;
}

int bSTIteratorNext(BSTIterator* obj) {
    struct TreeNode* node = obj->stack[--obj->size];
    pushLeft(obj, node->right);
    return node->val;
}

bool bSTIteratorHasNext(BSTIterator* obj) {
    return obj->size > 0;
}

void bSTIteratorFree(BSTIterator* obj) {
    free(obj->stack);
    free(obj);
}