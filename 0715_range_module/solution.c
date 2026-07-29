// LeetCode 0715 - Range Module
// https://leetcode.com/problems/range-module/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int* starts;
    int* ends;
    int size;
    int capacity;
} RangeModule;

RangeModule* rangeModuleCreate(void) {
    RangeModule* obj = (RangeModule*)calloc(1, sizeof(RangeModule));
    return obj;
}

static void ensureCap(RangeModule* obj, int need) {
    if (need <= obj->capacity) {
        return;
    }
    obj->capacity = obj->capacity ? obj->capacity * 2 : 8;
    while (obj->capacity < need) {
        obj->capacity *= 2;
    }
    obj->starts = (int*)realloc(obj->starts, (size_t)obj->capacity * sizeof(int));
    obj->ends = (int*)realloc(obj->ends, (size_t)obj->capacity * sizeof(int));
}

void rangeModuleAddRange(RangeModule* obj, int left, int right) {
    int* ns = (int*)malloc((size_t)(obj->size + 1) * sizeof(int));
    int* ne = (int*)malloc((size_t)(obj->size + 1) * sizeof(int));
    int nsize = 0;
    bool placed = false;
    for (int i = 0; i < obj->size; i++) {
        int start = obj->starts[i], end = obj->ends[i];
        if (end < left) {
            ns[nsize] = start;
            ne[nsize++] = end;
        } else if (right < start) {
            if (!placed) {
                ns[nsize] = left;
                ne[nsize++] = right;
                placed = true;
            }
            ns[nsize] = start;
            ne[nsize++] = end;
        } else {
            if (start < left) left = start;
            if (end > right) right = end;
        }
    }
    if (!placed) {
        ns[nsize] = left;
        ne[nsize++] = right;
    }
    free(obj->starts);
    free(obj->ends);
    obj->starts = ns;
    obj->ends = ne;
    obj->size = nsize;
    obj->capacity = nsize;
}

bool rangeModuleQueryRange(RangeModule* obj, int left, int right) {
    int lo = 0, hi = obj->size - 1, i = -1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (obj->starts[mid] <= left) {
            i = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    if (i < 0) {
        return false;
    }
    return obj->starts[i] <= left && right <= obj->ends[i];
}

void rangeModuleRemoveRange(RangeModule* obj, int left, int right) {
    int* ns = (int*)malloc((size_t)(obj->size * 2 + 1) * sizeof(int));
    int* ne = (int*)malloc((size_t)(obj->size * 2 + 1) * sizeof(int));
    int nsize = 0;
    for (int i = 0; i < obj->size; i++) {
        int start = obj->starts[i], end = obj->ends[i];
        if (end <= left || right <= start) {
            ns[nsize] = start;
            ne[nsize++] = end;
        } else {
            if (start < left) {
                ns[nsize] = start;
                ne[nsize++] = left;
            }
            if (right < end) {
                ns[nsize] = right;
                ne[nsize++] = end;
            }
        }
    }
    free(obj->starts);
    free(obj->ends);
    obj->starts = ns;
    obj->ends = ne;
    obj->size = nsize;
    obj->capacity = nsize;
}

void rangeModuleFree(RangeModule* obj) {
    free(obj->starts);
    free(obj->ends);
    free(obj);
}
