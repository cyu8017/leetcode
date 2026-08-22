// LeetCode 2526 - Find Consecutive Integers from a Data Stream
// https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int value;
    int k;
    int streak;
} DataStream;

DataStream* dataStreamCreate(int value, int k) {
    DataStream* obj = (DataStream*)malloc(sizeof(DataStream));
    obj->value = value;
    obj->k = k;
    obj->streak = 0;
    return obj;
}

bool dataStreamConsec(DataStream* obj, int num) {
    if (num == obj->value) obj->streak++;
    else obj->streak = 0;
    return obj->streak >= obj->k;
}

void dataStreamFree(DataStream* obj) {
    free(obj);
}
