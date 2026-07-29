// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

#include <stdbool.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct {
    int* values;
    int size;
    int capacity;
} FindElements;

static void recover(struct TreeNode* node, int value, FindElements* obj) {
    if (!node) return;
    node->val = value;
    if (obj->size >= obj->capacity) {
        obj->capacity *= 2;
        obj->values = (int*)realloc(obj->values, (size_t)obj->capacity * sizeof(int));
    }
    obj->values[obj->size++] = value;
    recover(node->left, 2 * value + 1, obj);
    recover(node->right, 2 * value + 2, obj);
}

FindElements* findElementsCreate(struct TreeNode* root) {
    FindElements* obj = (FindElements*)malloc(sizeof(FindElements));
    obj->capacity = 16;
    obj->size = 0;
    obj->values = (int*)malloc((size_t)obj->capacity * sizeof(int));
    recover(root, 0, obj);
    return obj;
}

bool findElementsFind(FindElements* obj, int target) {
    for (int i = 0; i < obj->size; i++) {
        if (obj->values[i] == target) return true;
    }
    return false;
}

void findElementsFree(FindElements* obj) {
    if (!obj) return;
    free(obj->values);
    free(obj);
}
