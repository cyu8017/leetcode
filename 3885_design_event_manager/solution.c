// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int p;
    int id;
} Pair3885;

typedef struct {
    Pair3885* heap;
    int size;
    int cap;
    int* prio;
    int prioCap;
} EventManager;

static void heapSwap3885(Pair3885* a, Pair3885* b) { Pair3885 t = *a; *a = *b; *b = t; }
static int pairLess3885(Pair3885 a, Pair3885 b) {
    if (a.p != b.p) return a.p < b.p;
    return a.id < b.id;
}
static void heapUp3885(EventManager* obj, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (!pairLess3885(obj->heap[i], obj->heap[p])) break;
        heapSwap3885(&obj->heap[i], &obj->heap[p]);
        i = p;
    }
}
static void heapDown3885(EventManager* obj, int i) {
    for (;;) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < obj->size && pairLess3885(obj->heap[l], obj->heap[best])) best = l;
        if (r < obj->size && pairLess3885(obj->heap[r], obj->heap[best])) best = r;
        if (best == i) break;
        heapSwap3885(&obj->heap[i], &obj->heap[best]);
        i = best;
    }
}
static void heapPush3885(EventManager* obj, Pair3885 x) {
    if (obj->size == obj->cap) {
        obj->cap = obj->cap ? obj->cap * 2 : 8;
        obj->heap = realloc(obj->heap, (size_t)obj->cap * sizeof(Pair3885));
    }
    obj->heap[obj->size] = x;
    heapUp3885(obj, obj->size++);
}
static void ensurePrio3885(EventManager* obj, int id) {
    if (id < obj->prioCap) return;
    int nc = id + 1;
    if (nc < 16) nc = 16;
    if (obj->prioCap * 2 > nc) nc = obj->prioCap * 2;
    obj->prio = realloc(obj->prio, (size_t)nc * sizeof(int));
    for (int i = obj->prioCap; i < nc; i++) obj->prio[i] = -1;
    obj->prioCap = nc;
}

EventManager* eventManagerCreate(int** events, int eventsSize, int* eventsColSize) {
    (void)eventsColSize;
    EventManager* obj = calloc(1, sizeof(EventManager));
    for (int i = 0; i < eventsSize; i++) {
        int eventId = events[i][0], priority = events[i][1];
        ensurePrio3885(obj, eventId);
        obj->prio[eventId] = priority;
        Pair3885 pr = {-priority, eventId};
        heapPush3885(obj, pr);
    }
    return obj;
}

void eventManagerUpdatePriority(EventManager* obj, int eventId, int newPriority) {
    ensurePrio3885(obj, eventId);
    obj->prio[eventId] = newPriority;
    Pair3885 pr = {-newPriority, eventId};
    heapPush3885(obj, pr);
}

int eventManagerPollHighest(EventManager* obj) {
    while (obj->size > 0) {
        Pair3885 top = obj->heap[0];
        obj->heap[0] = obj->heap[--obj->size];
        if (obj->size) heapDown3885(obj, 0);
        if (top.id < obj->prioCap && obj->prio[top.id] != -1 && -obj->prio[top.id] == top.p) {
            obj->prio[top.id] = -1;
            return top.id;
        }
    }
    return -1;
}

void eventManagerFree(EventManager* obj) {
    if (!obj) return;
    free(obj->heap);
    free(obj->prio);
    free(obj);
}
