// LeetCode 1705 - Maximum Number of Eaten Apples
// https://leetcode.com/problems/maximum-number-of-eaten-apples/

#include <stdlib.h>

typedef struct {
    int expire;
    int count;
} HeapItem;

static void heapSwap(HeapItem* a, HeapItem* b) {
    HeapItem tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(HeapItem* heap, int* size, HeapItem item) {
    int i = (*size)++;
    heap[i] = item;
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (heap[parent].expire <= heap[i].expire) {
            break;
        }
        heapSwap(&heap[parent], &heap[i]);
        i = parent;
    }
}

static HeapItem heapPop(HeapItem* heap, int* size) {
    HeapItem top = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0;
    for (;;) {
        int smallest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        if (left < *size && heap[left].expire < heap[smallest].expire) {
            smallest = left;
        }
        if (right < *size && heap[right].expire < heap[smallest].expire) {
            smallest = right;
        }
        if (smallest == i) {
            break;
        }
        heapSwap(&heap[smallest], &heap[i]);
        i = smallest;
    }
    return top;
}

int eatenApples(int* apples, int applesSize, int* days, int daysSize) {
    HeapItem* heap = (HeapItem*)malloc((applesSize + 1) * sizeof(HeapItem));
    int size = 0;
    int day = 0;
    int eaten = 0;
    while (day < applesSize || size > 0) {
        if (day < applesSize && apples[day] > 0) {
            HeapItem item = { day + days[day], apples[day] };
            heapPush(heap, &size, item);
        }
        while (size > 0 && heap[0].expire <= day) {
            heapPop(heap, &size);
        }
        if (size > 0) {
            HeapItem top = heapPop(heap, &size);
            eaten++;
            if (top.count > 1) {
                HeapItem item = { top.expire, top.count - 1 };
                heapPush(heap, &size, item);
            }
        }
        day++;
    }
    free(heap);
    return eaten;
}
