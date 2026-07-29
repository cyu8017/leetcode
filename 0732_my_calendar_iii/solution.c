// LeetCode 0732 - My Calendar III
// https://leetcode.com/problems/my-calendar-iii/

#include <stdlib.h>

typedef struct {
    int* times;
    int* deltas;
    int size;
    int capacity;
} MyCalendarThree;

MyCalendarThree* myCalendarThreeCreate(void) {
    return (MyCalendarThree*)calloc(1, sizeof(MyCalendarThree));
}

static int findTime(MyCalendarThree* obj, int time) {
    for (int i = 0; i < obj->size; i++) {
        if (obj->times[i] == time) {
            return i;
        }
    }
    return -1;
}

static int cmpPair(const void* a, const void* b) {
    return ((const int*)a)[0] - ((const int*)b)[0];
}

int myCalendarThreeBook(MyCalendarThree* obj, int startTime, int endTime) {
    int idx = findTime(obj, startTime);
    if (idx < 0) {
        if (obj->size == obj->capacity) {
            obj->capacity = obj->capacity ? obj->capacity * 2 : 8;
            obj->times = (int*)realloc(obj->times, (size_t)obj->capacity * sizeof(int));
            obj->deltas = (int*)realloc(obj->deltas, (size_t)obj->capacity * sizeof(int));
        }
        obj->times[obj->size] = startTime;
        obj->deltas[obj->size] = 1;
        obj->size++;
    } else {
        obj->deltas[idx]++;
    }
    idx = findTime(obj, endTime);
    if (idx < 0) {
        if (obj->size == obj->capacity) {
            obj->capacity = obj->capacity ? obj->capacity * 2 : 8;
            obj->times = (int*)realloc(obj->times, (size_t)obj->capacity * sizeof(int));
            obj->deltas = (int*)realloc(obj->deltas, (size_t)obj->capacity * sizeof(int));
        }
        obj->times[obj->size] = endTime;
        obj->deltas[obj->size] = -1;
        obj->size++;
    } else {
        obj->deltas[idx]--;
    }

    int* pairs = (int*)malloc((size_t)obj->size * 2 * sizeof(int));
    for (int i = 0; i < obj->size; i++) {
        pairs[i * 2] = obj->times[i];
        pairs[i * 2 + 1] = obj->deltas[i];
    }
    qsort(pairs, (size_t)obj->size, sizeof(int) * 2, cmpPair);
    int current = 0, best = 0;
    for (int i = 0; i < obj->size; i++) {
        current += pairs[i * 2 + 1];
        if (current > best) best = current;
    }
    free(pairs);
    return best;
}

void myCalendarThreeFree(MyCalendarThree* obj) {
    free(obj->times);
    free(obj->deltas);
    free(obj);
}
