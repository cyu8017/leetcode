// LeetCode 0919 - Complete Binary Tree Inserter
// https://leetcode.com/problems/complete-binary-tree-inserter/

#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct {
    struct TreeNode* root;
    struct TreeNode** queue;
    int head, tail, capacity;
} CBTInserter;

CBTInserter* cBTInserterCreate(struct TreeNode* root) {
    CBTInserter* obj = (CBTInserter*)malloc(sizeof(CBTInserter));
    obj->root = root;
    obj->capacity = 1024;
    obj->queue = (struct TreeNode**)malloc((size_t)obj->capacity * sizeof(struct TreeNode*));
    obj->head = obj->tail = 0;
    struct TreeNode** bfs = (struct TreeNode**)malloc(1024 * sizeof(struct TreeNode*));
    int bh = 0, bt = 0;
    bfs[bt++] = root;
    while (bh < bt) {
        struct TreeNode* node = bfs[bh++];
        if (node->left) bfs[bt++] = node->left;
        else { obj->queue[obj->tail++] = node; break; }
        if (node->right) bfs[bt++] = node->right;
        else { obj->queue[obj->tail++] = node; break; }
    }
    while (bh < bt) obj->queue[obj->tail++] = bfs[bh++];
    free(bfs);
    return obj;
}

int cBTInserterInsert(CBTInserter* obj, int val) {
    struct TreeNode* parent = obj->queue[obj->head];
    struct TreeNode* child = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    child->val = val; child->left = child->right = NULL;
    if (!parent->left) parent->left = child;
    else {
        parent->right = child;
        obj->head++;
    }
    if (obj->tail == obj->capacity) {
        obj->capacity *= 2;
        obj->queue = (struct TreeNode**)realloc(obj->queue, (size_t)obj->capacity * sizeof(struct TreeNode*));
    }
    obj->queue[obj->tail++] = child;
    return parent->val;
}

struct TreeNode* cBTInserterGet_root(CBTInserter* obj) {
    return obj->root;
}

void cBTInserterFree(CBTInserter* obj) {
    free(obj->queue);
    free(obj);
}
