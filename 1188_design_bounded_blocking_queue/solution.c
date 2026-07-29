// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>

typedef struct {
    int* buffer;
    int capacity;
    int head;
    int tail;
    int size;
    sem_t notFull;
    sem_t notEmpty;
    pthread_mutex_t lock;
} BoundedBlockingQueue;

BoundedBlockingQueue* boundedBlockingQueueCreate(int capacity) {
    BoundedBlockingQueue* obj = (BoundedBlockingQueue*)malloc(sizeof(BoundedBlockingQueue));
    obj->buffer = (int*)malloc((size_t)capacity * sizeof(int));
    obj->capacity = capacity;
    obj->head = obj->tail = obj->size = 0;
    sem_init(&obj->notFull, 0, capacity);
    sem_init(&obj->notEmpty, 0, 0);
    pthread_mutex_init(&obj->lock, NULL);
    return obj;
}

void boundedBlockingQueueEnqueue(BoundedBlockingQueue* obj, int element) {
    sem_wait(&obj->notFull);
    pthread_mutex_lock(&obj->lock);
    obj->buffer[obj->tail] = element;
    obj->tail = (obj->tail + 1) % obj->capacity;
    obj->size++;
    pthread_mutex_unlock(&obj->lock);
    sem_post(&obj->notEmpty);
}

int boundedBlockingQueueDequeue(BoundedBlockingQueue* obj) {
    sem_wait(&obj->notEmpty);
    pthread_mutex_lock(&obj->lock);
    int value = obj->buffer[obj->head];
    obj->head = (obj->head + 1) % obj->capacity;
    obj->size--;
    pthread_mutex_unlock(&obj->lock);
    sem_post(&obj->notFull);
    return value;
}

int boundedBlockingQueueSize(BoundedBlockingQueue* obj) {
    pthread_mutex_lock(&obj->lock);
    int value = obj->size;
    pthread_mutex_unlock(&obj->lock);
    return value;
}

void boundedBlockingQueueFree(BoundedBlockingQueue* obj) {
    if (!obj) return;
    free(obj->buffer);
    sem_destroy(&obj->notFull);
    sem_destroy(&obj->notEmpty);
    pthread_mutex_destroy(&obj->lock);
    free(obj);
}
