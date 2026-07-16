// LeetCode 0295 - Find Median from Data Stream
// https://leetcode.com/problems/find-median-from-data-stream/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int* data;
    int size;
    int capacity;
} IntHeap;

typedef struct {
    IntHeap small;
    IntHeap large;
} MedianFinder;

static void heapInit(IntHeap* heap) {
    heap->data = NULL;
    heap->size = 0;
    heap->capacity = 0;
}

static void heapFree(IntHeap* heap) {
    free(heap->data);
    heap->data = NULL;
    heap->size = 0;
    heap->capacity = 0;
}

static void heapEnsure(IntHeap* heap) {
    if (heap->size < heap->capacity) {
        return;
    }
    heap->capacity = heap->capacity == 0 ? 8 : heap->capacity * 2;
    heap->data = (int*)realloc(heap->data, (size_t)heap->capacity * sizeof(int));
}

static void maxHeapPush(IntHeap* heap, int value) {
    heapEnsure(heap);
    int index = heap->size++;
    heap->data[index] = value;
    while (index > 0) {
        int parent = (index - 1) / 2;
        if (heap->data[parent] >= heap->data[index]) {
            break;
        }
        int tmp = heap->data[parent];
        heap->data[parent] = heap->data[index];
        heap->data[index] = tmp;
        index = parent;
    }
}

static int maxHeapPop(IntHeap* heap) {
    int top = heap->data[0];
    heap->data[0] = heap->data[--heap->size];
    int index = 0;
    while (1) {
        int left = index * 2 + 1;
        int right = left + 1;
        int largest = index;
        if (left < heap->size && heap->data[left] > heap->data[largest]) {
            largest = left;
        }
        if (right < heap->size && heap->data[right] > heap->data[largest]) {
            largest = right;
        }
        if (largest == index) {
            break;
        }
        int tmp = heap->data[index];
        heap->data[index] = heap->data[largest];
        heap->data[largest] = tmp;
        index = largest;
    }
    return top;
}

static int maxHeapTop(IntHeap* heap) {
    return heap->data[0];
}

static void minHeapPush(IntHeap* heap, int value) {
    heapEnsure(heap);
    int index = heap->size++;
    heap->data[index] = value;
    while (index > 0) {
        int parent = (index - 1) / 2;
        if (heap->data[parent] <= heap->data[index]) {
            break;
        }
        int tmp = heap->data[parent];
        heap->data[parent] = heap->data[index];
        heap->data[index] = tmp;
        index = parent;
    }
}

static int minHeapPop(IntHeap* heap) {
    int top = heap->data[0];
    heap->data[0] = heap->data[--heap->size];
    int index = 0;
    while (1) {
        int left = index * 2 + 1;
        int right = left + 1;
        int smallest = index;
        if (left < heap->size && heap->data[left] < heap->data[smallest]) {
            smallest = left;
        }
        if (right < heap->size && heap->data[right] < heap->data[smallest]) {
            smallest = right;
        }
        if (smallest == index) {
            break;
        }
        int tmp = heap->data[index];
        heap->data[index] = heap->data[smallest];
        heap->data[smallest] = tmp;
        index = smallest;
    }
    return top;
}

static int minHeapTop(IntHeap* heap) {
    return heap->data[0];
}

MedianFinder* medianFinderCreate() {
    MedianFinder* obj = (MedianFinder*)malloc(sizeof(MedianFinder));
    heapInit(&obj->small);
    heapInit(&obj->large);
    return obj;
}

void medianFinderAddNum(MedianFinder* obj, int num) {
    maxHeapPush(&obj->small, num);
    minHeapPush(&obj->large, maxHeapPop(&obj->small));
    if (obj->large.size > obj->small.size) {
        maxHeapPush(&obj->small, minHeapPop(&obj->large));
    }
}

double medianFinderFindMedian(MedianFinder* obj) {
    if (obj->small.size > obj->large.size) {
        return (double)maxHeapTop(&obj->small);
    }
    return ((double)maxHeapTop(&obj->small) + (double)minHeapTop(&obj->large)) / 2.0;
}

void medianFinderFree(MedianFinder* obj) {
    heapFree(&obj->small);
    heapFree(&obj->large);
    free(obj);
}
