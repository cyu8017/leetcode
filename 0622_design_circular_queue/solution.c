// LeetCode 0622 - Design Circular Queue
// https://leetcode.com/problems/design-circular-queue/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int* data;
    int capacity;
    int head;
    int size;
} MyCircularQueue;

MyCircularQueue* myCircularQueueCreate(int k) {
    MyCircularQueue* obj = (MyCircularQueue*)malloc(sizeof(MyCircularQueue));
    obj->data = (int*)malloc((size_t)k * sizeof(int));
    obj->capacity = k;
    obj->head = 0;
    obj->size = 0;
    return obj;
}

bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
    if (obj->size == obj->capacity) {
        return false;
    }
    obj->data[(obj->head + obj->size) % obj->capacity] = value;
    obj->size++;
    return true;
}

bool myCircularQueueDeQueue(MyCircularQueue* obj) {
    if (obj->size == 0) {
        return false;
    }
    obj->head = (obj->head + 1) % obj->capacity;
    obj->size--;
    return true;
}

int myCircularQueueFront(MyCircularQueue* obj) {
    return obj->size == 0 ? -1 : obj->data[obj->head];
}

int myCircularQueueRear(MyCircularQueue* obj) {
    if (obj->size == 0) {
        return -1;
    }
    return obj->data[(obj->head + obj->size - 1) % obj->capacity];
}

bool myCircularQueueIsEmpty(MyCircularQueue* obj) {
    return obj->size == 0;
}

bool myCircularQueueIsFull(MyCircularQueue* obj) {
    return obj->size == obj->capacity;
}

void myCircularQueueFree(MyCircularQueue* obj) {
    free(obj->data);
    free(obj);
}
