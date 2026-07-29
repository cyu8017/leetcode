// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>

typedef struct {
    sem_t hydrogen;
    sem_t oxygen;
    pthread_mutex_t lock;
    int count;
} H2O;

H2O* h2OCreate(void) {
    H2O* obj = (H2O*)malloc(sizeof(H2O));
    sem_init(&obj->hydrogen, 0, 2);
    sem_init(&obj->oxygen, 0, 0);
    pthread_mutex_init(&obj->lock, NULL);
    obj->count = 0;
    return obj;
}

void h2OHydrogen(H2O* obj, void (*releaseHydrogen)(void)) {
    sem_wait(&obj->hydrogen);
    pthread_mutex_lock(&obj->lock);
    obj->count++;
    if (obj->count == 2) sem_post(&obj->oxygen);
    pthread_mutex_unlock(&obj->lock);
    releaseHydrogen();
}

void h2OOxygen(H2O* obj, void (*releaseOxygen)(void)) {
    sem_wait(&obj->oxygen);
    releaseOxygen();
    pthread_mutex_lock(&obj->lock);
    obj->count = 0;
    sem_post(&obj->hydrogen);
    sem_post(&obj->hydrogen);
    pthread_mutex_unlock(&obj->lock);
}

void h2OFree(H2O* obj) {
    if (!obj) return;
    sem_destroy(&obj->hydrogen);
    sem_destroy(&obj->oxygen);
    pthread_mutex_destroy(&obj->lock);
    free(obj);
}
