// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int m;
    int k;
    int* stream;
    int size;
    int capacity;
} MKAverage;

MKAverage* mKAverageCreate(int m, int k) {
    MKAverage* obj = (MKAverage*)malloc(sizeof(MKAverage));
    obj->m = m;
    obj->k = k;
    obj->stream = NULL;
    obj->size = 0;
    obj->capacity = 0;
    return obj;
}

void mKAverageAddElement(MKAverage* obj, int num) {
    if (obj->size == obj->capacity) {
        obj->capacity = obj->capacity ? obj->capacity * 2 : 16;
        obj->stream = (int*)realloc(obj->stream, (size_t)obj->capacity * sizeof(int));
    }
    obj->stream[obj->size++] = num;
}

static int cmpInt(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

int mKAverageCalculateMKAverage(MKAverage* obj) {
    if (obj->size < obj->m) return -1;
    int* window = (int*)malloc((size_t)obj->m * sizeof(int));
    memcpy(window, obj->stream + (obj->size - obj->m), (size_t)obj->m * sizeof(int));
    qsort(window, (size_t)obj->m, sizeof(int), cmpInt);
    long long sum = 0;
    for (int i = obj->k; i < obj->m - obj->k; i++) sum += window[i];
    free(window);
    return (int)(sum / (obj->m - 2 * obj->k));
}

void mKAverageFree(MKAverage* obj) {
    if (!obj) return;
    free(obj->stream);
    free(obj);
}
