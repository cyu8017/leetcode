// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

#include <pthread.h>
#include <stdlib.h>

typedef struct {
    int n;
    int current;
    pthread_mutex_t lock;
    pthread_cond_t cond;
} FizzBuzz;

FizzBuzz* fizzBuzzCreate(int n) {
    FizzBuzz* obj = (FizzBuzz*)malloc(sizeof(FizzBuzz));
    obj->n = n;
    obj->current = 1;
    pthread_mutex_init(&obj->lock, NULL);
    pthread_cond_init(&obj->cond, NULL);
    return obj;
}

static void runLoop(FizzBuzz* obj, int (*predicate)(int), void (*action)(void)) {
    pthread_mutex_lock(&obj->lock);
    while (obj->current <= obj->n) {
        if (predicate(obj->current)) {
            action();
            obj->current++;
            pthread_cond_broadcast(&obj->cond);
        } else {
            pthread_cond_wait(&obj->cond, &obj->lock);
        }
    }
    pthread_mutex_unlock(&obj->lock);
}

static int isFizz(int x) { return x % 3 == 0 && x % 5 != 0; }
static int isBuzz(int x) { return x % 5 == 0 && x % 3 != 0; }
static int isFizzBuzz(int x) { return x % 15 == 0; }
static int isNumber(int x) { return x % 3 != 0 && x % 5 != 0; }

void fizzBuzzFizz(FizzBuzz* obj, void (*printFizz)(void)) {
    runLoop(obj, isFizz, printFizz);
}

void fizzBuzzBuzz(FizzBuzz* obj, void (*printBuzz)(void)) {
    runLoop(obj, isBuzz, printBuzz);
}

void fizzBuzzFizzbuzz(FizzBuzz* obj, void (*printFizzBuzz)(void)) {
    runLoop(obj, isFizzBuzz, printFizzBuzz);
}

void fizzBuzzNumber(FizzBuzz* obj, void (*printNumber)(int)) {
    pthread_mutex_lock(&obj->lock);
    while (obj->current <= obj->n) {
        if (isNumber(obj->current)) {
            printNumber(obj->current);
            obj->current++;
            pthread_cond_broadcast(&obj->cond);
        } else {
            pthread_cond_wait(&obj->cond, &obj->lock);
        }
    }
    pthread_mutex_unlock(&obj->lock);
}

void fizzBuzzFree(FizzBuzz* obj) {
    if (!obj) return;
    pthread_mutex_destroy(&obj->lock);
    pthread_cond_destroy(&obj->cond);
    free(obj);
}
