// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int* values;
    int size;
    int capacity;
} Skiplist;

static int lowerBound(int* arr, int size, int target) {
    int lo = 0, hi = size;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (arr[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

Skiplist* skiplistCreate(void) {
    Skiplist* obj = (Skiplist*)malloc(sizeof(Skiplist));
    obj->capacity = 16;
    obj->size = 0;
    obj->values = (int*)malloc((size_t)obj->capacity * sizeof(int));
    return obj;
}

bool skiplistSearch(Skiplist* obj, int target) {
    int i = lowerBound(obj->values, obj->size, target);
    return i < obj->size && obj->values[i] == target;
}

void skiplistAdd(Skiplist* obj, int num) {
    int i = lowerBound(obj->values, obj->size, num);
    if (obj->size >= obj->capacity) {
        obj->capacity *= 2;
        obj->values = (int*)realloc(obj->values, (size_t)obj->capacity * sizeof(int));
    }
    for (int j = obj->size; j > i; j--) obj->values[j] = obj->values[j - 1];
    obj->values[i] = num;
    obj->size++;
}

bool skiplistErase(Skiplist* obj, int num) {
    int i = lowerBound(obj->values, obj->size, num);
    if (i == obj->size || obj->values[i] != num) return false;
    for (int j = i + 1; j < obj->size; j++) obj->values[j - 1] = obj->values[j];
    obj->size--;
    return true;
}

void skiplistFree(Skiplist* obj) {
    if (!obj) return;
    free(obj->values);
    free(obj);
}
