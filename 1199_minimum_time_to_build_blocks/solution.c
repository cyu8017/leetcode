// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

#include <stdlib.h>

static void heapify(int* heap, int size) {
    for (int i = size / 2 - 1; i >= 0; i--) {
        int smallest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        if (left < size && heap[left] < heap[smallest]) smallest = left;
        if (right < size && heap[right] < heap[smallest]) smallest = right;
        if (smallest != i) {
            int tmp = heap[i];
            heap[i] = heap[smallest];
            heap[smallest] = tmp;
        }
    }
}

static int popHeap(int* heap, int* size) {
    int top = heap[0];
    heap[0] = heap[--(*size)];
    heapify(heap, *size);
    return top;
}

static void pushHeap(int* heap, int* size, int value) {
    int i = (*size)++;
    heap[i] = value;
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (heap[parent] <= heap[i]) break;
        int tmp = heap[i];
        heap[i] = heap[parent];
        heap[parent] = tmp;
        i = parent;
    }
}

int minBuildTime(int* blocks, int blocksSize, int split) {
    int* heap = (int*)malloc((size_t)blocksSize * sizeof(int));
    for (int i = 0; i < blocksSize; i++) heap[i] = blocks[i];
    int size = blocksSize;
    heapify(heap, size);
    while (size > 1) {
        popHeap(heap, &size);
        int second = popHeap(heap, &size);
        pushHeap(heap, &size, second + split);
    }
    int ans = heap[0];
    free(heap);
    return ans;
}
