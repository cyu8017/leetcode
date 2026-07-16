// LeetCode 0346 - Moving Average from Data Stream
// https://leetcode.com/problems/moving-average-from-data-stream/

#include <stdlib.h>

typedef struct {
    int size;
    int* values;
    int count;
    int head;
    long long total;
} MovingAverage;

MovingAverage* movingAverageCreate(int size) {
    MovingAverage* obj = (MovingAverage*)calloc(1, sizeof(MovingAverage));
    obj->size = size;
    obj->values = (int*)calloc((size_t)size, sizeof(int));
    return obj;
}

double movingAverageNext(MovingAverage* obj, int val) {
    if (obj->count < obj->size) {
        obj->values[obj->count] = val;
        obj->total += val;
        obj->count += 1;
        return (double)obj->total / (double)obj->count;
    }

    obj->total -= obj->values[obj->head];
    obj->values[obj->head] = val;
    obj->total += val;
    obj->head = (obj->head + 1) % obj->size;
    return (double)obj->total / (double)obj->size;
}

void movingAverageFree(MovingAverage* obj) {
    free(obj->values);
    free(obj);
}
