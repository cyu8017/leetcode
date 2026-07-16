// LeetCode 0232 - Implement Queue using Stacks
// https://leetcode.com/problems/implement-queue-using-stacks/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int* data;
    int size;
    int capacity;
} IntStack;

typedef struct {
    IntStack input;
    IntStack output;
} MyQueue;

static void stackInit(IntStack* stack) {
    stack->capacity = 16;
    stack->data = (int*)malloc((size_t)stack->capacity * sizeof(int));
    stack->size = 0;
}

static void stackPush(IntStack* stack, int x) {
    if (stack->size == stack->capacity) {
        stack->capacity *= 2;
        stack->data = (int*)realloc(stack->data, (size_t)stack->capacity * sizeof(int));
    }
    stack->data[stack->size++] = x;
}

static int stackPop(IntStack* stack) {
    return stack->data[--stack->size];
}

static bool stackEmpty(IntStack* stack) {
    return stack->size == 0;
}

static void stackFree(IntStack* stack) {
    free(stack->data);
    stack->data = NULL;
    stack->size = 0;
    stack->capacity = 0;
}

static void move(MyQueue* obj) {
    if (stackEmpty(&obj->output)) {
        while (!stackEmpty(&obj->input)) {
            stackPush(&obj->output, stackPop(&obj->input));
        }
    }
}

MyQueue* myQueueCreate() {
    MyQueue* obj = (MyQueue*)malloc(sizeof(MyQueue));
    stackInit(&obj->input);
    stackInit(&obj->output);
    return obj;
}

void myQueuePush(MyQueue* obj, int x) {
    stackPush(&obj->input, x);
}

int myQueuePop(MyQueue* obj) {
    move(obj);
    return stackPop(&obj->output);
}

int myQueuePeek(MyQueue* obj) {
    move(obj);
    return obj->output.data[obj->output.size - 1];
}

bool myQueueEmpty(MyQueue* obj) {
    return stackEmpty(&obj->input) && stackEmpty(&obj->output);
}

void myQueueFree(MyQueue* obj) {
    stackFree(&obj->input);
    stackFree(&obj->output);
    free(obj);
}
