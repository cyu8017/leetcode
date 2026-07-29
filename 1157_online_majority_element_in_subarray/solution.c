// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int* arr;
    int arrSize;
    int** pos;
    int* posSize;
    int* posCap;
    int maxVal;
} MajorityChecker;

MajorityChecker* majorityCheckerCreate(int* arr, int arrSize) {
    MajorityChecker* obj = (MajorityChecker*)malloc(sizeof(MajorityChecker));
    obj->arr = arr;
    obj->arrSize = arrSize;
    int maxVal = 0;
    for (int i = 0; i < arrSize; i++) if (arr[i] > maxVal) maxVal = arr[i];
    obj->maxVal = maxVal;
    obj->pos = (int**)calloc((size_t)(maxVal + 1), sizeof(int*));
    obj->posSize = (int*)calloc((size_t)(maxVal + 1), sizeof(int));
    obj->posCap = (int*)calloc((size_t)(maxVal + 1), sizeof(int));
    for (int i = 0; i < arrSize; i++) {
        int x = arr[i];
        if (obj->posSize[x] >= obj->posCap[x]) {
            obj->posCap[x] = obj->posCap[x] ? obj->posCap[x] * 2 : 4;
            obj->pos[x] = (int*)realloc(obj->pos[x], (size_t)obj->posCap[x] * sizeof(int));
        }
        obj->pos[x][obj->posSize[x]++] = i;
    }
    return obj;
}

static int lowerBound(int* a, int n, int t) {
    int lo = 0, hi = n;
    while (lo < hi) { int mid = (lo + hi) / 2; if (a[mid] < t) lo = mid + 1; else hi = mid; }
    return lo;
}
static int upperBound(int* a, int n, int t) {
    int lo = 0, hi = n;
    while (lo < hi) { int mid = (lo + hi) / 2; if (a[mid] <= t) lo = mid + 1; else hi = mid; }
    return lo;
}

int majorityCheckerQuery(MajorityChecker* obj, int left, int right, int threshold) {
    int candidate = 0, count = 0;
    for (int i = left; i <= right; i++) {
        if (count == 0) candidate = obj->arr[i];
        count += obj->arr[i] == candidate ? 1 : -1;
    }
    int* locs = obj->pos[candidate];
    int n = obj->posSize[candidate];
    int freq = upperBound(locs, n, right) - lowerBound(locs, n, left);
    return freq >= threshold ? candidate : -1;
}

void majorityCheckerFree(MajorityChecker* obj) {
    if (!obj) return;
    for (int i = 0; i <= obj->maxVal; i++) free(obj->pos[i]);
    free(obj->pos); free(obj->posSize); free(obj->posCap); free(obj);
}
