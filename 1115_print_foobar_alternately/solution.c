// LeetCode 1115 - Print FooBar Alternately
// https://leetcode.com/problems/print-foobar-alternately/

#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>

typedef struct {
    int n;
    sem_t fooSem;
    sem_t barSem;
} FooBar;

FooBar* fooBarCreate(int n) {
    FooBar* obj = (FooBar*)malloc(sizeof(FooBar));
    obj->n = n;
    sem_init(&obj->fooSem, 0, 1);
    sem_init(&obj->barSem, 0, 0);
    return obj;
}

void fooBarFoo(FooBar* obj, void (*printFoo)(void)) {
    for (int i = 0; i < obj->n; i++) {
        sem_wait(&obj->fooSem);
        printFoo();
        sem_post(&obj->barSem);
    }
}

void fooBarBar(FooBar* obj, void (*printBar)(void)) {
    for (int i = 0; i < obj->n; i++) {
        sem_wait(&obj->barSem);
        printBar();
        sem_post(&obj->fooSem);
    }
}

void fooBarFree(FooBar* obj) {
    if (!obj) return;
    sem_destroy(&obj->fooSem);
    sem_destroy(&obj->barSem);
    free(obj);
}
