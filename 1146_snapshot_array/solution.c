// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

#include <stdlib.h>

typedef struct { int snapId; int val; } HistEntry;

typedef struct {
    HistEntry* data;
    int size;
    int capacity;
} Hist;

typedef struct {
    int snap_id;
    Hist* arr;
    int length;
} SnapshotArray;

SnapshotArray* snapshotArrayCreate(int length) {
    SnapshotArray* obj = (SnapshotArray*)malloc(sizeof(SnapshotArray));
    obj->snap_id = 0;
    obj->length = length;
    obj->arr = (Hist*)calloc((size_t)length, sizeof(Hist));
    for (int i = 0; i < length; i++) {
        obj->arr[i].capacity = 4;
        obj->arr[i].size = 1;
        obj->arr[i].data = (HistEntry*)malloc(4 * sizeof(HistEntry));
        obj->arr[i].data[0] = (HistEntry){0, 0};
    }
    return obj;
}

void snapshotArraySet(SnapshotArray* obj, int index, int val) {
    Hist* h = &obj->arr[index];
    if (h->data[h->size - 1].snapId == obj->snap_id) {
        h->data[h->size - 1].val = val;
    } else {
        if (h->size >= h->capacity) {
            h->capacity *= 2;
            h->data = (HistEntry*)realloc(h->data, (size_t)h->capacity * sizeof(HistEntry));
        }
        h->data[h->size++] = (HistEntry){obj->snap_id, val};
    }
}

int snapshotArraySnap(SnapshotArray* obj) {
    return obj->snap_id++;
}

int snapshotArrayGet(SnapshotArray* obj, int index, int snap_id) {
    Hist* h = &obj->arr[index];
    int lo = 0, hi = h->size - 1, ans = 0;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (h->data[mid].snapId <= snap_id) { ans = mid; lo = mid + 1; }
        else hi = mid - 1;
    }
    return h->data[ans].val;
}

void snapshotArrayFree(SnapshotArray* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->length; i++) free(obj->arr[i].data);
    free(obj->arr);
    free(obj);
}
