// LeetCode 1845 - Seat Reservation Manager
// https://leetcode.com/problems/seat-reservation-manager/

#include <stdlib.h>

typedef struct {
    int* data;
    int size;
    int capacity;
} MinHeap;

typedef struct {
    MinHeap available;
} SeatManager;

static void heapEnsure(MinHeap* h) {
    if (h->size < h->capacity) return;
    h->capacity = h->capacity ? h->capacity * 2 : 16;
    h->data = (int*)realloc(h->data, (size_t)h->capacity * sizeof(int));
}

static void heapPush(MinHeap* h, int value) {
    heapEnsure(h);
    int i = h->size++;
    h->data[i] = value;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p] <= h->data[i]) break;
        int t = h->data[p];
        h->data[p] = h->data[i];
        h->data[i] = t;
        i = p;
    }
}

static int heapPop(MinHeap* h) {
    int top = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = l + 1, best = i;
        if (l < h->size && h->data[l] < h->data[best]) best = l;
        if (r < h->size && h->data[r] < h->data[best]) best = r;
        if (best == i) break;
        int t = h->data[i];
        h->data[i] = h->data[best];
        h->data[best] = t;
        i = best;
    }
    return top;
}

SeatManager* seatManagerCreate(int n) {
    SeatManager* obj = (SeatManager*)malloc(sizeof(SeatManager));
    obj->available.data = NULL;
    obj->available.size = 0;
    obj->available.capacity = 0;
    for (int i = 1; i <= n; i++) heapPush(&obj->available, i);
    return obj;
}

int seatManagerReserve(SeatManager* obj) {
    return heapPop(&obj->available);
}

void seatManagerUnreserve(SeatManager* obj, int seatNumber) {
    heapPush(&obj->available, seatNumber);
}

void seatManagerFree(SeatManager* obj) {
    if (!obj) return;
    free(obj->available.data);
    free(obj);
}
