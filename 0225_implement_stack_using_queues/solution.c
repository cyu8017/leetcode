// LeetCode 0225 - Implement Stack using Queues
// https://leetcode.com/problems/implement-stack-using-queues/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int* data;
    int head;
    int size;
    int capacity;
} MyStack;

MyStack* myStackCreate() {
    MyStack* obj = (MyStack*)malloc(sizeof(MyStack));
    obj->capacity = 16;
    obj->data = (int*)malloc((size_t)obj->capacity * sizeof(int));
    obj->head = 0;
    obj->size = 0;
    return obj;
}

void myStackPush(MyStack* obj, int x) {
    if (obj->size == obj->capacity) {
        obj->capacity *= 2;
        obj->data = (int*)realloc(obj->data, (size_t)obj->capacity * sizeof(int));
    }
    obj->data[(obj->head + obj->size) % obj->capacity] = x;
    obj->size++;
    for (int i = 0; i < obj->size - 1; ++i) {
        int front = obj->data[obj->head];
        obj->head = (obj->head + 1) % obj->capacity;
        obj->data[(obj->head + obj->size - 1) % obj->capacity] = front;
    }
}

int myStackPop(MyStack* obj) {
    int value = obj->data[obj->head];
    obj->head = (obj->head + 1) % obj->capacity;
    obj->size--;
    return value;
}

int myStackTop(MyStack* obj) {
    return obj->data[obj->head];
}

bool myStackEmpty(MyStack* obj) {
    return obj->size == 0;
}

void myStackFree(MyStack* obj) {
    free(obj->data);
    free(obj);
}
