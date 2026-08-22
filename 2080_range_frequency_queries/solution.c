// LeetCode 2080 - Range Frequency Queries
// https://leetcode.com/problems/range-frequency-queries/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int** pos;
    int* cnt;
    int* caps;
} RangeFreqQuery;

RangeFreqQuery* rangeFreqQueryCreate(int* arr, int arrSize) {
    RangeFreqQuery* obj = (RangeFreqQuery*)calloc(1, sizeof(RangeFreqQuery));
    obj->pos = (int**)calloc(10001, sizeof(int*));
    obj->cnt = (int*)calloc(10001, sizeof(int));
    obj->caps = (int*)calloc(10001, sizeof(int));
    for (int i = 0; i < arrSize; i++) {
        int v = arr[i];
        if (obj->cnt[v] == obj->caps[v]) {
            obj->caps[v] = obj->caps[v] ? obj->caps[v] * 2 : 4;
            obj->pos[v] = (int*)realloc(obj->pos[v], (size_t)obj->caps[v] * sizeof(int));
        }
        obj->pos[v][obj->cnt[v]++] = i;
    }
    return obj;
}

int rangeFreqQueryQuery(RangeFreqQuery* obj, int left, int right, int value) {
    int* p = obj->pos[value];
    int n = obj->cnt[value];
    if (!p || n == 0) return 0;
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (p[mid] < left) lo = mid + 1;
        else hi = mid;
    }
    int L = lo;
    lo = 0; hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (p[mid] <= right) lo = mid + 1;
        else hi = mid;
    }
    return lo - L;
}

void rangeFreqQueryFree(RangeFreqQuery* obj) {
    if (!obj) return;
    for (int i = 0; i <= 10000; i++) free(obj->pos[i]);
    free(obj->pos); free(obj->cnt); free(obj->caps); free(obj);
}
