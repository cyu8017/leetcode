// LeetCode 1670 - Design Front Middle Back Queue
// https://leetcode.com/problems/design-front-middle-back-queue/

#include <stdlib.h>

typedef struct {
    int* data;
    int head;
    int size;
    int capacity;
} Deque;

static void dqInit(Deque* d) {
    d->capacity = 16;
    d->data = (int*)malloc((size_t)d->capacity * sizeof(int));
    d->head = 0;
    d->size = 0;
}

static void dqEnsure(Deque* d) {
    if (d->size < d->capacity) return;
    int* nd = (int*)malloc((size_t)d->capacity * 2 * sizeof(int));
    for (int i = 0; i < d->size; i++) nd[i] = d->data[(d->head + i) % d->capacity];
    free(d->data);
    d->data = nd;
    d->head = 0;
    d->capacity *= 2;
}

static void dqPushFront(Deque* d, int v) {
    dqEnsure(d);
    d->head = (d->head - 1 + d->capacity) % d->capacity;
    d->data[d->head] = v;
    d->size++;
}

static void dqPushBack(Deque* d, int v) {
    dqEnsure(d);
    d->data[(d->head + d->size) % d->capacity] = v;
    d->size++;
}

static int dqPopFront(Deque* d) {
    int v = d->data[d->head];
    d->head = (d->head + 1) % d->capacity;
    d->size--;
    return v;
}

static int dqPopBack(Deque* d) {
    d->size--;
    return d->data[(d->head + d->size) % d->capacity];
}

typedef struct {
    Deque l;
    Deque r;
} FrontMiddleBackQueue;

static void bal(FrontMiddleBackQueue* obj) {
    while (obj->l.size > obj->r.size + 1) {
        dqPushFront(&obj->r, dqPopBack(&obj->l));
    }
    while (obj->r.size > obj->l.size) {
        dqPushBack(&obj->l, dqPopFront(&obj->r));
    }
}

FrontMiddleBackQueue* frontMiddleBackQueueCreate(void) {
    FrontMiddleBackQueue* obj = (FrontMiddleBackQueue*)malloc(sizeof(FrontMiddleBackQueue));
    dqInit(&obj->l);
    dqInit(&obj->r);
    return obj;
}

void frontMiddleBackQueuePushFront(FrontMiddleBackQueue* obj, int val) {
    dqPushFront(&obj->l, val);
    bal(obj);
}

void frontMiddleBackQueuePushMiddle(FrontMiddleBackQueue* obj, int val) {
    if (obj->l.size > obj->r.size) dqPushFront(&obj->r, dqPopBack(&obj->l));
    dqPushBack(&obj->l, val);
}

void frontMiddleBackQueuePushBack(FrontMiddleBackQueue* obj, int val) {
    dqPushBack(&obj->r, val);
    bal(obj);
}

int frontMiddleBackQueuePopFront(FrontMiddleBackQueue* obj) {
    if (obj->l.size == 0) return -1;
    int v = dqPopFront(&obj->l);
    bal(obj);
    return v;
}

int frontMiddleBackQueuePopMiddle(FrontMiddleBackQueue* obj) {
    if (obj->l.size == 0) return -1;
    int v = dqPopBack(&obj->l);
    bal(obj);
    return v;
}

int frontMiddleBackQueuePopBack(FrontMiddleBackQueue* obj) {
    if (obj->l.size == 0) return -1;
    int v = obj->r.size ? dqPopBack(&obj->r) : dqPopBack(&obj->l);
    bal(obj);
    return v;
}

void frontMiddleBackQueueFree(FrontMiddleBackQueue* obj) {
    free(obj->l.data);
    free(obj->r.data);
    free(obj);
}
