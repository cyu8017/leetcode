// LeetCode 2336 - Smallest Number in Infinite Set
// https://leetcode.com/problems/smallest-number-in-infinite-set/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct {
    int next;
    int* heap;
    int heapSize;
    int heapCap;
    bool* added;
    int addedCap;
} SmallestInfiniteSet;

static void heapPush(SmallestInfiniteSet* obj, int x) {
    if (obj->heapSize >= obj->heapCap) {
        obj->heapCap = obj->heapCap ? obj->heapCap * 2 : 16;
        obj->heap = (int*)realloc(obj->heap, (size_t)obj->heapCap * sizeof(int));
    }
    int i = obj->heapSize++;
    obj->heap[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (obj->heap[p] <= obj->heap[i]) break;
        int t = obj->heap[p]; obj->heap[p] = obj->heap[i]; obj->heap[i] = t;
        i = p;
    }
}

static int heapPop(SmallestInfiniteSet* obj) {
    int res = obj->heap[0];
    obj->heap[0] = obj->heap[--obj->heapSize];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, sm = i;
        if (l < obj->heapSize && obj->heap[l] < obj->heap[sm]) sm = l;
        if (r < obj->heapSize && obj->heap[r] < obj->heap[sm]) sm = r;
        if (sm == i) break;
        int t = obj->heap[i]; obj->heap[i] = obj->heap[sm]; obj->heap[sm] = t;
        i = sm;
    }
    return res;
}

SmallestInfiniteSet* smallestInfiniteSetCreate(void) {
    SmallestInfiniteSet* obj = (SmallestInfiniteSet*)calloc(1, sizeof(SmallestInfiniteSet));
    obj->next = 1;
    obj->addedCap = 1024;
    obj->added = (bool*)calloc((size_t)obj->addedCap, sizeof(bool));
    return obj;
}

int smallestInfiniteSetPopSmallest(SmallestInfiniteSet* obj) {
    if (obj->heapSize > 0) {
        int x = heapPop(obj);
        if (x < obj->addedCap) obj->added[x] = false;
        return x;
    }
    return obj->next++;
}

void smallestInfiniteSetAddBack(SmallestInfiniteSet* obj, int num) {
    if (num < obj->next) {
        if (num >= obj->addedCap) {
            int nc = num + 1;
            obj->added = (bool*)realloc(obj->added, (size_t)nc * sizeof(bool));
            memset(obj->added + obj->addedCap, 0, (size_t)(nc - obj->addedCap) * sizeof(bool));
            obj->addedCap = nc;
        }
        if (!obj->added[num]) {
            obj->added[num] = true;
            heapPush(obj, num);
        }
    }
}

void smallestInfiniteSetFree(SmallestInfiniteSet* obj) {
    if (!obj) return;
    free(obj->heap);
    free(obj->added);
    free(obj);
}
