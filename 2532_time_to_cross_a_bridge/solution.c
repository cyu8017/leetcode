// LeetCode 2532 - Time to Cross a Bridge
// https://leetcode.com/problems/time-to-cross-a-bridge/

#include <stdlib.h>

typedef struct {
    int idx, efficiency, leftToRight, pickOld, rightToLeft, putNew;
} Worker2532;

typedef struct {
    int time;
    Worker2532 w;
    int side;
} Event2532;

static int lessWait(Worker2532 a, Worker2532 b) {
    if (a.efficiency != b.efficiency) return a.efficiency > b.efficiency;
    return a.idx > b.idx;
}

static void pushWait(Worker2532* h, int* n, Worker2532 x) {
    int i = (*n)++;
    h[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (!lessWait(h[i], h[p])) break;
        Worker2532 t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static Worker2532 popWait(Worker2532* h, int* n) {
    Worker2532 res = h[0];
    h[0] = h[--(*n)];
    int i = 0;
    for (;;) {
        int l = i * 2 + 1, r = l + 1, best = i;
        if (l < *n && lessWait(h[l], h[best])) best = l;
        if (r < *n && lessWait(h[r], h[best])) best = r;
        if (best == i) break;
        Worker2532 t = h[i]; h[i] = h[best]; h[best] = t;
        i = best;
    }
    return res;
}

static void pushEv(Event2532* h, int* n, Event2532 x) {
    int i = (*n)++;
    h[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p].time <= h[i].time) break;
        Event2532 t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static Event2532 popEv(Event2532* h, int* n) {
    Event2532 res = h[0];
    h[0] = h[--(*n)];
    int i = 0;
    for (;;) {
        int l = i * 2 + 1, r = l + 1, best = i;
        if (l < *n && h[l].time < h[best].time) best = l;
        if (r < *n && h[r].time < h[best].time) best = r;
        if (best == i) break;
        Event2532 t = h[i]; h[i] = h[best]; h[best] = t;
        i = best;
    }
    return res;
}

int findCrossingTime(int n, int k, int** time, int timeSize, int* timeColSize) {
    (void)timeSize; (void)timeColSize;
    Worker2532* left = (Worker2532*)malloc((size_t)(k + 5) * sizeof(Worker2532));
    Worker2532* right = (Worker2532*)malloc((size_t)(k + 5) * sizeof(Worker2532));
    Event2532* events = (Event2532*)malloc((size_t)(n * 2 + k + 5) * sizeof(Event2532));
    int ln = 0, rn = 0, en = 0;
    for (int i = 0; i < k; i++) {
        Worker2532 w = {i, time[i][0] + time[i][2], time[i][0], time[i][1], time[i][2], time[i][3]};
        pushWait(left, &ln, w);
    }
    int cur = 0, remain = n, done = 0, bridgeFree = 0;
    while (done < n) {
        while (en > 0 && events[0].time <= cur) {
            Event2532 e = popEv(events, &en);
            if (e.side == 0) pushWait(left, &ln, e.w);
            else pushWait(right, &rn, e.w);
        }
        if (cur < bridgeFree) { cur = bridgeFree; continue; }
        if (rn > 0) {
            Worker2532 w = popWait(right, &rn);
            cur += w.rightToLeft;
            bridgeFree = cur;
            pushEv(events, &en, (Event2532){cur + w.putNew, w, 0});
            done++;
            continue;
        }
        if (ln > 0 && remain > 0) {
            Worker2532 w = popWait(left, &ln);
            cur += w.leftToRight;
            bridgeFree = cur;
            remain--;
            pushEv(events, &en, (Event2532){cur + w.pickOld, w, 1});
            continue;
        }
        if (en == 0) break;
        cur = events[0].time;
    }
    free(left); free(right); free(events);
    return cur;
}
