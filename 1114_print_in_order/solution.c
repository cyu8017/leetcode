// LeetCode 1114 - Print in Order
// https://leetcode.com/problems/print-in-order/

#include <pthread.h>
#include <stdlib.h>

typedef struct {
    pthread_mutex_t m2;
    pthread_mutex_t m3;
} Foo;

Foo* fooCreate(void) {
    Foo* obj = (Foo*)malloc(sizeof(Foo));
    pthread_mutex_init(&obj->m2, NULL);
    pthread_mutex_init(&obj->m3, NULL);
    pthread_mutex_lock(&obj->m2);
    pthread_mutex_lock(&obj->m3);
    return obj;
}

void fooFirst(Foo* obj, void (*printFirst)(void)) {
    printFirst();
    pthread_mutex_unlock(&obj->m2);
}

void fooSecond(Foo* obj, void (*printSecond)(void)) {
    pthread_mutex_lock(&obj->m2);
    printSecond();
    pthread_mutex_unlock(&obj->m3);
}

void fooThird(Foo* obj, void (*printThird)(void)) {
    pthread_mutex_lock(&obj->m3);
    printThird();
}

void fooFree(Foo* obj) {
    if (!obj) return;
    pthread_mutex_destroy(&obj->m2);
    pthread_mutex_destroy(&obj->m3);
    free(obj);
}
