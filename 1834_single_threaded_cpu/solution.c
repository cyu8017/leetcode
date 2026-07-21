// LeetCode 1834 - Single-Threaded CPU
// https://leetcode.com/problems/single-threaded-cpu/

#include <stdlib.h>

typedef struct {
    int enqueue;
    int process;
    int index;
} Task;

typedef struct {
    int process;
    int index;
} HeapItem;

typedef struct {
    HeapItem* data;
    int size;
    int capacity;
} MinHeap;

static int cmpTask(const void* a, const void* b) {
    const Task* x = (const Task*)a;
    const Task* y = (const Task*)b;
    if (x->enqueue != y->enqueue) return (x->enqueue > y->enqueue) - (x->enqueue < y->enqueue);
    return (x->index > y->index) - (x->index < y->index);
}

static void heapEnsure(MinHeap* h) {
    if (h->size < h->capacity) return;
    h->capacity = h->capacity ? h->capacity * 2 : 16;
    h->data = (HeapItem*)realloc(h->data, (size_t)h->capacity * sizeof(HeapItem));
}

static int heapLess(HeapItem a, HeapItem b) {
    if (a.process != b.process) return a.process < b.process;
    return a.index < b.index;
}

static void heapPush(MinHeap* h, int process, int index) {
    heapEnsure(h);
    int i = h->size++;
    h->data[i].process = process;
    h->data[i].index = index;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (!heapLess(h->data[i], h->data[p])) break;
        HeapItem t = h->data[p];
        h->data[p] = h->data[i];
        h->data[i] = t;
        i = p;
    }
}

static HeapItem heapPop(MinHeap* h) {
    HeapItem top = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = l + 1, best = i;
        if (l < h->size && heapLess(h->data[l], h->data[best])) best = l;
        if (r < h->size && heapLess(h->data[r], h->data[best])) best = r;
        if (best == i) break;
        HeapItem t = h->data[i];
        h->data[i] = h->data[best];
        h->data[best] = t;
        i = best;
    }
    return top;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getOrder(int** tasks, int tasksSize, int* tasksColSize, int* returnSize) {
    (void)tasksColSize;
    Task* indexed = (Task*)malloc((size_t)tasksSize * sizeof(Task));
    for (int i = 0; i < tasksSize; i++) {
        indexed[i].enqueue = tasks[i][0];
        indexed[i].process = tasks[i][1];
        indexed[i].index = i;
    }
    qsort(indexed, (size_t)tasksSize, sizeof(Task), cmpTask);

    MinHeap heap = {0};
    int* order = (int*)malloc((size_t)tasksSize * sizeof(int));
    int out = 0;
    int i = 0;
    long long time = 0;

    while (i < tasksSize || heap.size) {
        if (i < tasksSize && !heap.size) {
            if (time < indexed[i].enqueue) time = indexed[i].enqueue;
        }
        while (i < tasksSize && indexed[i].enqueue <= time) {
            heapPush(&heap, indexed[i].process, indexed[i].index);
            i++;
        }
        HeapItem cur = heapPop(&heap);
        time += cur.process;
        order[out++] = cur.index;
    }

    free(heap.data);
    free(indexed);
    *returnSize = tasksSize;
    return order;
}
