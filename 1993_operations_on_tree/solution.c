// LeetCode 1993 - Operations on Tree
// https://leetcode.com/problems/operations-on-tree/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct {
    int* locked;
    int* parent;
    int** children;
    int* childSize;
    int* childCap;
    int n;
} LockingTree;

LockingTree* lockingTreeCreate(int* parent, int parentSize) {
    LockingTree* obj = (LockingTree*)malloc(sizeof(LockingTree));
    obj->n = parentSize;
    obj->parent = (int*)malloc((size_t)parentSize * sizeof(int));
    memcpy(obj->parent, parent, (size_t)parentSize * sizeof(int));
    obj->locked = (int*)malloc((size_t)parentSize * sizeof(int));
    for (int i = 0; i < parentSize; i++) obj->locked[i] = -1;
    obj->children = (int**)calloc((size_t)parentSize, sizeof(int*));
    obj->childSize = (int*)calloc((size_t)parentSize, sizeof(int));
    obj->childCap = (int*)calloc((size_t)parentSize, sizeof(int));
    for (int son = 1; son < parentSize; son++) {
        int fa = parent[son];
        if (obj->childSize[fa] == obj->childCap[fa]) {
            obj->childCap[fa] = obj->childCap[fa] ? obj->childCap[fa] * 2 : 4;
            obj->children[fa] = (int*)realloc(obj->children[fa], (size_t)obj->childCap[fa] * sizeof(int));
        }
        obj->children[fa][obj->childSize[fa]++] = son;
    }
    return obj;
}

bool lockingTreeLock(LockingTree* obj, int num, int user) {
    if (obj->locked[num] == -1) {
        obj->locked[num] = user;
        return true;
    }
    return false;
}

bool lockingTreeUnlock(LockingTree* obj, int num, int user) {
    if (obj->locked[num] == user) {
        obj->locked[num] = -1;
        return true;
    }
    return false;
}

static void unlockDescendants(LockingTree* obj, int u, int* find) {
    for (int i = 0; i < obj->childSize[u]; i++) {
        int v = obj->children[u][i];
        if (obj->locked[v] != -1) {
            obj->locked[v] = -1;
            *find = 1;
        }
        unlockDescendants(obj, v, find);
    }
}

bool lockingTreeUpgrade(LockingTree* obj, int num, int user) {
    int x = num;
    while (x != -1) {
        if (obj->locked[x] != -1) return false;
        x = obj->parent[x];
    }
    int find = 0;
    unlockDescendants(obj, num, &find);
    if (!find) return false;
    obj->locked[num] = user;
    return true;
}

void lockingTreeFree(LockingTree* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->n; i++) free(obj->children[i]);
    free(obj->children);
    free(obj->childSize);
    free(obj->childCap);
    free(obj->locked);
    free(obj->parent);
    free(obj);
}
