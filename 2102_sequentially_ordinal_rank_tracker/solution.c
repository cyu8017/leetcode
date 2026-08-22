// LeetCode 2102 - Sequentially Ordinal Rank Tracker
// https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

#include <stdlib.h>
#include <string.h>

typedef struct { char* name; int score; } Loc2102;

typedef struct {
    Loc2102* a;
    int n, cap;
} Heap2102;

typedef struct {
    Heap2102 best; /* min-heap of top k: worse is smaller */
    Heap2102 rest; /* max-heap of the rest */
    int k;
} SORTracker;

static int worseThan(Loc2102 a, Loc2102 b) {
    /* a is worse than b (should be lower in ranking / smaller in min-heap of best) */
    if (a.score != b.score) return a.score < b.score;
    return strcmp(a.name, b.name) > 0;
}

static int betterThan(Loc2102 a, Loc2102 b) {
    if (a.score != b.score) return a.score > b.score;
    return strcmp(a.name, b.name) < 0;
}

static void heapPushMin(Heap2102* h, Loc2102 x) {
    if (h->n == h->cap) { h->cap = h->cap ? h->cap * 2 : 8; h->a = (Loc2102*)realloc(h->a, (size_t)h->cap * sizeof(Loc2102)); }
    int i = h->n++;
    h->a[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (!worseThan(h->a[i], h->a[p])) break;
        Loc2102 t = h->a[p]; h->a[p] = h->a[i]; h->a[i] = t;
        i = p;
    }
}

static Loc2102 heapPopMin(Heap2102* h) {
    Loc2102 top = h->a[0];
    h->a[0] = h->a[--h->n];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, r = l + 1, sm = i;
        if (l < h->n && worseThan(h->a[l], h->a[sm])) sm = l;
        if (r < h->n && worseThan(h->a[r], h->a[sm])) sm = r;
        if (sm == i) break;
        Loc2102 t = h->a[i]; h->a[i] = h->a[sm]; h->a[sm] = t;
        i = sm;
    }
    return top;
}

static void heapPushMax(Heap2102* h, Loc2102 x) {
    if (h->n == h->cap) { h->cap = h->cap ? h->cap * 2 : 8; h->a = (Loc2102*)realloc(h->a, (size_t)h->cap * sizeof(Loc2102)); }
    int i = h->n++;
    h->a[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (!betterThan(h->a[i], h->a[p])) break;
        Loc2102 t = h->a[p]; h->a[p] = h->a[i]; h->a[i] = t;
        i = p;
    }
}

static Loc2102 heapPopMax(Heap2102* h) {
    Loc2102 top = h->a[0];
    h->a[0] = h->a[--h->n];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, r = l + 1, sm = i;
        if (l < h->n && betterThan(h->a[l], h->a[sm])) sm = l;
        if (r < h->n && betterThan(h->a[r], h->a[sm])) sm = r;
        if (sm == i) break;
        Loc2102 t = h->a[i]; h->a[i] = h->a[sm]; h->a[sm] = t;
        i = sm;
    }
    return top;
}

SORTracker* sORTrackerCreate(void) {
    return (SORTracker*)calloc(1, sizeof(SORTracker));
}

void sORTrackerAdd(SORTracker* obj, char* name, int score) {
    Loc2102 item;
    item.name = strdup(name);
    item.score = score;
    heapPushMin(&obj->best, item);
    if (obj->best.n > obj->k) heapPushMax(&obj->rest, heapPopMin(&obj->best));
}

char* sORTrackerGet(SORTracker* obj) {
    obj->k++;
    if (obj->rest.n > 0) heapPushMin(&obj->best, heapPopMax(&obj->rest));
    return obj->best.a[0].name;
}

void sORTrackerFree(SORTracker* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->best.n; i++) free(obj->best.a[i].name);
    for (int i = 0; i < obj->rest.n; i++) free(obj->rest.a[i].name);
    free(obj->best.a); free(obj->rest.a); free(obj);
}
