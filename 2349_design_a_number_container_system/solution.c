// LeetCode 2349 - Design a Number Container System
// https://leetcode.com/problems/design-a-number-container-system/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct {
    int* data;
    int size;
    int cap;
} MinHeap;

typedef struct {
    int key;
    int val;
    bool used;
} MapEntry;

typedef struct {
    MapEntry* idx;
    int idxCap;
    int idxCount;
    MapEntry* heaps; /* key=number -> heap index in heapArr */
    int heapsCap;
    int heapsCount;
    MinHeap* heapArr;
    int heapArrSize;
    int heapArrCap;
} NumberContainers;

static unsigned hashInt(int k) { return (unsigned)k * 2654435761u; }

static void ensureMap(MapEntry** e, int* cap, int count) {
    if (*cap == 0) {
        *cap = 1024;
        *e = (MapEntry*)calloc((size_t)*cap, sizeof(MapEntry));
        return;
    }
    if (count * 2 < *cap) return;
    int ncap = *cap * 2;
    MapEntry* ne = (MapEntry*)calloc((size_t)ncap, sizeof(MapEntry));
    for (int i = 0; i < *cap; i++) if ((*e)[i].used) {
        unsigned h = hashInt((*e)[i].key);
        int j = (int)(h & (unsigned)(ncap - 1));
        while (ne[j].used) j = (j + 1) & (ncap - 1);
        ne[j] = (*e)[i];
    }
    free(*e); *e = ne; *cap = ncap;
}

static int mapGet(MapEntry* e, int cap, int key, bool* found) {
    if (cap == 0) { *found = false; return 0; }
    unsigned h = hashInt(key);
    int j = (int)(h & (unsigned)(cap - 1));
    for (;;) {
        if (!e[j].used) { *found = false; return j; }
        if (e[j].key == key) { *found = true; return j; }
        j = (j + 1) & (cap - 1);
    }
}

static void heapPush(MinHeap* h, int x) {
    if (h->size >= h->cap) {
        h->cap = h->cap ? h->cap * 2 : 8;
        h->data = (int*)realloc(h->data, (size_t)h->cap * sizeof(int));
    }
    int i = h->size++;
    h->data[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p] <= h->data[i]) break;
        int t = h->data[p]; h->data[p] = h->data[i]; h->data[i] = t;
        i = p;
    }
}

static int heapPop(MinHeap* h) {
    int res = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2*i+1, r = 2*i+2, sm = i;
        if (l < h->size && h->data[l] < h->data[sm]) sm = l;
        if (r < h->size && h->data[r] < h->data[sm]) sm = r;
        if (sm == i) break;
        int t = h->data[i]; h->data[i] = h->data[sm]; h->data[sm] = t;
        i = sm;
    }
    return res;
}

NumberContainers* numberContainersCreate(void) {
    return (NumberContainers*)calloc(1, sizeof(NumberContainers));
}

void numberContainersChange(NumberContainers* obj, int index, int number) {
    ensureMap(&obj->idx, &obj->idxCap, obj->idxCount);
    bool found;
    int j = mapGet(obj->idx, obj->idxCap, index, &found);
    if (!found) { obj->idx[j].used = true; obj->idx[j].key = index; obj->idxCount++; }
    obj->idx[j].val = number;

    ensureMap(&obj->heaps, &obj->heapsCap, obj->heapsCount);
    j = mapGet(obj->heaps, obj->heapsCap, number, &found);
    int hi;
    if (!found) {
        if (obj->heapArrSize >= obj->heapArrCap) {
            obj->heapArrCap = obj->heapArrCap ? obj->heapArrCap * 2 : 8;
            obj->heapArr = (MinHeap*)realloc(obj->heapArr, (size_t)obj->heapArrCap * sizeof(MinHeap));
        }
        hi = obj->heapArrSize++;
        memset(&obj->heapArr[hi], 0, sizeof(MinHeap));
        obj->heaps[j].used = true;
        obj->heaps[j].key = number;
        obj->heaps[j].val = hi;
        obj->heapsCount++;
    } else hi = obj->heaps[j].val;
    heapPush(&obj->heapArr[hi], index);
}

int numberContainersFind(NumberContainers* obj, int number) {
    bool found;
    int j = mapGet(obj->heaps, obj->heapsCap, number, &found);
    if (!found) return -1;
    MinHeap* h = &obj->heapArr[obj->heaps[j].val];
    while (h->size > 0) {
        int i = h->data[0];
        int ij = mapGet(obj->idx, obj->idxCap, i, &found);
        if (found && obj->idx[ij].val == number) return i;
        heapPop(h);
    }
    return -1;
}

void numberContainersFree(NumberContainers* obj) {
    if (!obj) return;
    free(obj->idx);
    free(obj->heaps);
    for (int i = 0; i < obj->heapArrSize; i++) free(obj->heapArr[i].data);
    free(obj->heapArr);
    free(obj);
}
