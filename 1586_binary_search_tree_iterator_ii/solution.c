// LeetCode 1586 - Binary Search Tree Iterator II
// https://leetcode.com/problems/binary-search-tree-iterator-ii/

#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct {
    int* values;
    int size;
    int index;
} BSTIterator;

BSTIterator* bSTIteratorCreate(struct TreeNode* root) {
    BSTIterator* obj = (BSTIterator*)malloc(sizeof(BSTIterator));
    obj->values = (int*)malloc(100000 * sizeof(int));
    obj->size = 0;
    obj->index = -1;
    struct TreeNode** stack = (struct TreeNode**)malloc(100000 * sizeof(struct TreeNode*));
    int top = 0;
    while (top > 0 || root) {
        while (root) {
            stack[top++] = root;
            root = root->left;
        }
        root = stack[--top];
        obj->values[obj->size++] = root->val;
        root = root->right;
    }
    free(stack);
    return obj;
}

bool bSTIteratorHasNext(BSTIterator* obj) {
    return obj->index + 1 < obj->size;
}

int bSTIteratorNext(BSTIterator* obj) {
    return obj->values[++obj->index];
}

bool bSTIteratorHasPrev(BSTIterator* obj) {
    return obj->index > 0;
}

int bSTIteratorPrev(BSTIterator* obj) {
    return obj->values[--obj->index];
}

void bSTIteratorFree(BSTIterator* obj) {
    free(obj->values);
    free(obj);
}
