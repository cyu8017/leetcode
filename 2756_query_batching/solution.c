// LeetCode 2756 - Query Batching
// https://leetcode.com/problems/query-batching/
// JS QueryBatcher design stand-in.

#include <stdlib.h>

typedef void** (*QueryMultipleFn)(void** queries, int n, int* outSize);
typedef void (*ResolveFn)(void* result);

typedef struct {
    QueryMultipleFn queryMultiple;
    int t;
    void** pending;
    ResolveFn* resolve;
    int size;
    int cap;
} QueryBatcher;

QueryBatcher* queryBatcherCreate(QueryMultipleFn queryMultiple, int t) {
    QueryBatcher* q = (QueryBatcher*)calloc(1, sizeof(QueryBatcher));
    q->queryMultiple = queryMultiple;
    q->t = t;
    q->cap = 8;
    q->pending = (void**)malloc(q->cap * sizeof(void*));
    q->resolve = (ResolveFn*)malloc(q->cap * sizeof(ResolveFn));
    return q;
}

void queryBatcherAddQuery(QueryBatcher* q, void* query, ResolveFn resolve) {
    if (q->size == q->cap) {
        q->cap *= 2;
        q->pending = (void**)realloc(q->pending, q->cap * sizeof(void*));
        q->resolve = (ResolveFn*)realloc(q->resolve, q->cap * sizeof(ResolveFn));
    }
    q->pending[q->size] = query;
    q->resolve[q->size] = resolve;
    q->size++;
}

void queryBatcherFree(QueryBatcher* q) {
    if (!q) return;
    free(q->pending);
    free(q->resolve);
    free(q);
}
