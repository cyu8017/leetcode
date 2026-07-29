// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

#include <pthread.h>
#include <stdlib.h>

typedef struct {
    pthread_mutex_t forks[5];
} DiningPhilosophers;

DiningPhilosophers* diningPhilosophersCreate(void) {
    DiningPhilosophers* obj = (DiningPhilosophers*)malloc(sizeof(DiningPhilosophers));
    for (int i = 0; i < 5; i++) pthread_mutex_init(&obj->forks[i], NULL);
    return obj;
}

void diningPhilosophersWantsToEat(DiningPhilosophers* obj, int philosopher,
    void (*pickLeftFork)(void), void (*pickRightFork)(void), void (*eat)(void),
    void (*putLeftFork)(void), void (*putRightFork)(void)) {
    int left = philosopher;
    int right = (philosopher + 1) % 5;
    int first = philosopher % 2 == 0 ? left : right;
    int second = philosopher % 2 == 0 ? right : left;
    pthread_mutex_lock(&obj->forks[first]);
    pthread_mutex_lock(&obj->forks[second]);
    pickLeftFork();
    pickRightFork();
    eat();
    putLeftFork();
    putRightFork();
    pthread_mutex_unlock(&obj->forks[second]);
    pthread_mutex_unlock(&obj->forks[first]);
}

void diningPhilosophersFree(DiningPhilosophers* obj) {
    if (!obj) return;
    for (int i = 0; i < 5; i++) pthread_mutex_destroy(&obj->forks[i]);
    free(obj);
}
