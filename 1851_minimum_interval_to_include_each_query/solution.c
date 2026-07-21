// LeetCode 1851 - Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int size;
    int right;
} HeapItem;

typedef struct {
    int value;
    int index;
} QueryItem;

static void swapHeap(HeapItem* a, HeapItem* b) {
    HeapItem t = *a;
    *a = *b;
    *b = t;
}

static void heapPush(HeapItem* heap, int* heapSize, int size, int right) {
    int i = (*heapSize)++;
    heap[i].size = size;
    heap[i].right = right;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (heap[p].size < heap[i].size ||
            (heap[p].size == heap[i].size && heap[p].right <= heap[i].right)) {
            break;
        }
        swapHeap(&heap[p], &heap[i]);
        i = p;
    }
}

static void heapPop(HeapItem* heap, int* heapSize) {
    heap[0] = heap[--(*heapSize)];
    int i = 0;
    while (1) {
        int l = i * 2 + 1, r = i * 2 + 2, best = i;
        if (l < *heapSize &&
            (heap[l].size < heap[best].size ||
             (heap[l].size == heap[best].size && heap[l].right < heap[best].right))) {
            best = l;
        }
        if (r < *heapSize &&
            (heap[r].size < heap[best].size ||
             (heap[r].size == heap[best].size && heap[r].right < heap[best].right))) {
            best = r;
        }
        if (best == i) break;
        swapHeap(&heap[i], &heap[best]);
        i = best;
    }
}

static int cmpInterval(const void* a, const void* b) {
    const int* const* aa = (const int* const*)a;
    const int* const* bb = (const int* const*)b;
    if ((*aa)[0] != (*bb)[0]) return (*aa)[0] - (*bb)[0];
    return (*aa)[1] - (*bb)[1];
}

static int cmpQuery(const void* a, const void* b) {
    const QueryItem* aa = (const QueryItem*)a;
    const QueryItem* bb = (const QueryItem*)b;
    if (aa->value != bb->value) return aa->value - bb->value;
    return aa->index - bb->index;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minInterval(int** intervals, int intervalsSize, int* intervalsColSize, int* queries,
                 int queriesSize, int* returnSize) {
    (void)intervalsColSize;
    int** sorted = (int**)malloc((size_t)intervalsSize * sizeof(int*));
    for (int i = 0; i < intervalsSize; i++) sorted[i] = intervals[i];
    qsort(sorted, (size_t)intervalsSize, sizeof(int*), cmpInterval);

    QueryItem* indexed = (QueryItem*)malloc((size_t)queriesSize * sizeof(QueryItem));
    for (int i = 0; i < queriesSize; i++) {
        indexed[i].value = queries[i];
        indexed[i].index = i;
    }
    qsort(indexed, (size_t)queriesSize, sizeof(QueryItem), cmpQuery);

    HeapItem* heap = (HeapItem*)malloc((size_t)(intervalsSize + 1) * sizeof(HeapItem));
    int heapSize = 0;
    int* answer = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) answer[i] = -1;

    int intervalIdx = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        int query = indexed[qi].value;
        while (intervalIdx < intervalsSize && sorted[intervalIdx][0] <= query) {
            int left = sorted[intervalIdx][0];
            int right = sorted[intervalIdx][1];
            heapPush(heap, &heapSize, right - left + 1, right);
            intervalIdx++;
        }
        while (heapSize > 0 && heap[0].right < query) {
            heapPop(heap, &heapSize);
        }
        if (heapSize > 0) {
            answer[indexed[qi].index] = heap[0].size;
        }
    }

    free(sorted);
    free(indexed);
    free(heap);
    *returnSize = queriesSize;
    return answer;
}
