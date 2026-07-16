// LeetCode 0341 - Flatten Nested List Iterator
// https://leetcode.com/problems/flatten-nested-list-iterator/

#include <stdbool.h>
#include <stdlib.h>

struct NestedInteger {
    int isInteger;
    int integer;
    struct NestedInteger* children;
    int childrenSize;
};

typedef struct {
    struct NestedInteger** nodes;
    int* indices;
    int size;
    int capacity;
} NestedIterator;

static void nestedIteratorEnsure(NestedIterator* iter) {
    if (iter->size < iter->capacity) {
        return;
    }
    iter->capacity = iter->capacity == 0 ? 8 : iter->capacity * 2;
    iter->nodes = (struct NestedInteger**)realloc(
        iter->nodes, (size_t)iter->capacity * sizeof(struct NestedInteger*));
    iter->indices = (int*)realloc(iter->indices, (size_t)iter->capacity * sizeof(int));
}

static void nestedIteratorPush(NestedIterator* iter, struct NestedInteger* node, int index) {
    nestedIteratorEnsure(iter);
    iter->nodes[iter->size] = node;
    iter->indices[iter->size] = index;
    iter->size += 1;
}

static void nestedIteratorPop(NestedIterator* iter) {
    if (iter->size > 0) {
        iter->size -= 1;
    }
}

static struct NestedInteger* nestedIteratorTop(NestedIterator* iter) {
    return iter->nodes[iter->size - 1];
}

static int nestedIteratorTopIndex(NestedIterator* iter) {
    return iter->indices[iter->size - 1];
}

static void nestedIteratorSetTopIndex(NestedIterator* iter, int index) {
    iter->indices[iter->size - 1] = index;
}

static void nestedIteratorPrepareNext(NestedIterator* iter);

static int nestedIteratorAdvance(NestedIterator* iter, struct NestedInteger* items, int itemsSize) {
    for (int index = itemsSize - 1; index >= 0; --index) {
        nestedIteratorPush(iter, &items[index], 0);
    }
    nestedIteratorPrepareNext(iter);
    struct NestedInteger* current = nestedIteratorTop(iter);
    nestedIteratorPop(iter);
    if (current->isInteger) {
        return current->integer;
    }
    return nestedIteratorAdvance(iter, current->children, current->childrenSize);
}

static void nestedIteratorPrepareNext(NestedIterator* iter) {
    while (iter->size > 0) {
        struct NestedInteger* current = nestedIteratorTop(iter);
        int index = nestedIteratorTopIndex(iter);
        if (current->isInteger) {
            return;
        }
        if (index >= current->childrenSize) {
            nestedIteratorPop(iter);
            continue;
        }
        nestedIteratorSetTopIndex(iter, index + 1);
        nestedIteratorPush(iter, &current->children[index], 0);
    }
}

NestedIterator* nestedIteratorCreate(struct NestedInteger** nestedList, int nestedListSize) {
    NestedIterator* iter = (NestedIterator*)calloc(1, sizeof(NestedIterator));
    for (int index = nestedListSize - 1; index >= 0; --index) {
        nestedIteratorPush(iter, nestedList[index], 0);
    }
    return iter;
}

int nestedIteratorNext(NestedIterator* iter) {
    struct NestedInteger* current = nestedIteratorTop(iter);
    nestedIteratorPop(iter);
    if (current->isInteger) {
        return current->integer;
    }
    return nestedIteratorAdvance(iter, current->children, current->childrenSize);
}

bool nestedIteratorHasNext(NestedIterator* iter) {
    nestedIteratorPrepareNext(iter);
    return iter->size > 0;
}

void nestedIteratorFree(NestedIterator* iter) {
    free(iter->nodes);
    free(iter->indices);
    free(iter);
}
