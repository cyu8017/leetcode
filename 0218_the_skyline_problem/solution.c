// LeetCode 0218 - The Skyline Problem
// https://leetcode.com/problems/the-skyline-problem/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int negH;
    int end;
} HeapItem;

typedef struct {
    HeapItem* data;
    int size;
    int capacity;
} MinHeap;

static void heapInit(MinHeap* heap) {
    heap->capacity = 16;
    heap->size = 0;
    heap->data = (HeapItem*)malloc((size_t)heap->capacity * sizeof(HeapItem));
}

static void heapFree(MinHeap* heap) {
    free(heap->data);
    heap->data = NULL;
    heap->size = 0;
    heap->capacity = 0;
}

static void heapSwap(HeapItem* a, HeapItem* b) {
    HeapItem temp = *a;
    *a = *b;
    *b = temp;
}

static void heapPush(MinHeap* heap, HeapItem item) {
    if (heap->size >= heap->capacity) {
        heap->capacity *= 2;
        heap->data = (HeapItem*)realloc(heap->data, (size_t)heap->capacity * sizeof(HeapItem));
    }
    int index = heap->size++;
    heap->data[index] = item;
    while (index > 0) {
        int parent = (index - 1) / 2;
        if (heap->data[parent].negH <= heap->data[index].negH) {
            break;
        }
        heapSwap(&heap->data[parent], &heap->data[index]);
        index = parent;
    }
}

static HeapItem heapPop(MinHeap* heap) {
    HeapItem top = heap->data[0];
    heap->data[0] = heap->data[--heap->size];
    int index = 0;
    while (1) {
        int smallest = index;
        int left = index * 2 + 1;
        int right = index * 2 + 2;
        if (left < heap->size && heap->data[left].negH < heap->data[smallest].negH) {
            smallest = left;
        }
        if (right < heap->size && heap->data[right].negH < heap->data[smallest].negH) {
            smallest = right;
        }
        if (smallest == index) {
            break;
        }
        heapSwap(&heap->data[smallest], &heap->data[index]);
        index = smallest;
    }
    return top;
}

static HeapItem heapPeek(MinHeap* heap) {
    return heap->data[0];
}

typedef struct {
    int x;
    int negH;
    int end;
} Event;

static int compareEvents(const void* a, const void* b) {
    const Event* ea = (const Event*)a;
    const Event* eb = (const Event*)b;
    if (ea->x != eb->x) {
        return ea->x - eb->x;
    }
    return ea->negH - eb->negH;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 */
int** getSkyline(int** buildings, int buildingsSize, int* buildingsColSize, int* returnSize, int** returnColumnSizes) {
    Event* events = (Event*)malloc((size_t)(buildingsSize * 2) * sizeof(Event));
    int eventCount = 0;
    for (int i = 0; i < buildingsSize; i++) {
        events[eventCount++] = (Event){ buildings[i][0], -buildings[i][2], buildings[i][1] };
        events[eventCount++] = (Event){ buildings[i][1], 0, 0 };
    }
    qsort(events, (size_t)eventCount, sizeof(Event), compareEvents);

    int capacity = 16;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)capacity * sizeof(int));
    int count = 0;

    MinHeap live;
    heapInit(&live);
    heapPush(&live, (HeapItem){ 0, 2147483647 });

    for (int i = 0; i < eventCount; i++) {
        int x = events[i].x;
        int negH = events[i].negH;
        int end = events[i].end;
        while (live.size > 0 && heapPeek(&live).end <= x) {
            heapPop(&live);
        }
        if (negH != 0) {
            heapPush(&live, (HeapItem){ negH, end });
        }
        int height = -heapPeek(&live).negH;
        if (count == 0 || result[count - 1][1] != height) {
            if (count >= capacity) {
                capacity *= 2;
                result = (int**)realloc(result, (size_t)capacity * sizeof(int*));
                colSizes = (int*)realloc(colSizes, (size_t)capacity * sizeof(int));
            }
            result[count] = (int*)malloc(2 * sizeof(int));
            result[count][0] = x;
            result[count][1] = height;
            colSizes[count] = 2;
            count++;
        }
    }

    free(events);
    heapFree(&live);
    *returnSize = count;
    *returnColumnSizes = (int*)realloc(colSizes, (size_t)count * sizeof(int));
    result = (int**)realloc(result, (size_t)count * sizeof(int*));
    return result;
}
