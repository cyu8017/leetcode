// LeetCode 0703 - Kth Largest Element in a Stream
// https://leetcode.com/problems/kth-largest-element-in-a-stream/

#include <stdlib.h>

typedef struct {
    int* data;
    int size;
    int capacity;
    int k;
} KthLargest;

static void heapSwap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

static void heapSiftUp(KthLargest* obj, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (obj->data[p] <= obj->data[i]) {
            break;
        }
        heapSwap(&obj->data[p], &obj->data[i]);
        i = p;
    }
}

static void heapSiftDown(KthLargest* obj, int i) {
    while (1) {
        int l = i * 2 + 1;
        int r = l + 1;
        int smallest = i;
        if (l < obj->size && obj->data[l] < obj->data[smallest]) {
            smallest = l;
        }
        if (r < obj->size && obj->data[r] < obj->data[smallest]) {
            smallest = r;
        }
        if (smallest == i) {
            break;
        }
        heapSwap(&obj->data[i], &obj->data[smallest]);
        i = smallest;
    }
}

static void heapPush(KthLargest* obj, int val) {
    if (obj->size == obj->capacity) {
        obj->capacity = obj->capacity ? obj->capacity * 2 : 8;
        obj->data = (int*)realloc(obj->data, (size_t)obj->capacity * sizeof(int));
    }
    obj->data[obj->size] = val;
    heapSiftUp(obj, obj->size++);
}

static void heapPop(KthLargest* obj) {
    obj->data[0] = obj->data[--obj->size];
    heapSiftDown(obj, 0);
}

KthLargest* kthLargestCreate(int k, int* nums, int numsSize) {
    KthLargest* obj = (KthLargest*)malloc(sizeof(KthLargest));
    obj->k = k;
    obj->data = NULL;
    obj->size = 0;
    obj->capacity = 0;
    for (int i = 0; i < numsSize; i++) {
        heapPush(obj, nums[i]);
        if (obj->size > k) {
            heapPop(obj);
        }
    }
    return obj;
}

int kthLargestAdd(KthLargest* obj, int val) {
    heapPush(obj, val);
    if (obj->size > obj->k) {
        heapPop(obj);
    }
    return obj->data[0];
}

void kthLargestFree(KthLargest* obj) {
    free(obj->data);
    free(obj);
}
