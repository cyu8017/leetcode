// LeetCode 1942 - The Number of the Smallest Unoccupied Chair
// https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

#include <stdlib.h>

typedef struct { int time; int chair; } Leave;
typedef struct { int arrive; int leave; int idx; } Friend;

static int cmpFriend(const void* a, const void* b) {
    return ((const Friend*)a)->arrive - ((const Friend*)b)->arrive;
}

static void minHeapPushI(int* h, int* sz, int v) {
    int i = (*sz)++;
    h[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] <= h[i]) break;
        int t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}

static int minHeapPopI(int* h, int* sz) {
    int top = h[0];
    h[0] = h[--(*sz)];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < *sz && h[l] < h[best]) best = l;
        if (r < *sz && h[r] < h[best]) best = r;
        if (best == i) break;
        int t = h[i]; h[i] = h[best]; h[best] = t;
        i = best;
    }
    return top;
}

static void leavePush(Leave* h, int* sz, Leave v) {
    int i = (*sz)++;
    h[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p].time <= h[i].time) break;
        Leave t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}

static Leave leavePop(Leave* h, int* sz) {
    Leave top = h[0];
    h[0] = h[--(*sz)];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < *sz && h[l].time < h[best].time) best = l;
        if (r < *sz && h[r].time < h[best].time) best = r;
        if (best == i) break;
        Leave t = h[i]; h[i] = h[best]; h[best] = t;
        i = best;
    }
    return top;
}

int smallestChair(int** times, int timesSize, int* timesColSize, int targetFriend) {
    (void)timesColSize;
    Friend* arr = (Friend*)malloc((size_t)timesSize * sizeof(Friend));
    for (int i = 0; i < timesSize; i++) {
        arr[i].arrive = times[i][0];
        arr[i].leave = times[i][1];
        arr[i].idx = i;
    }
    qsort(arr, (size_t)timesSize, sizeof(Friend), cmpFriend);
    int* freeChairs = (int*)malloc((size_t)timesSize * sizeof(int));
    int freeSz = 0, nextChair = 0;
    Leave* leaving = (Leave*)malloc((size_t)timesSize * sizeof(Leave));
    int leaveSz = 0;
    for (int t = 0; t < timesSize; t++) {
        int arrv = arr[t].arrive, leave = arr[t].leave, i = arr[t].idx;
        while (leaveSz && leaving[0].time <= arrv) {
            Leave L = leavePop(leaving, &leaveSz);
            minHeapPushI(freeChairs, &freeSz, L.chair);
        }
        int chair;
        if (freeSz) chair = minHeapPopI(freeChairs, &freeSz);
        else chair = nextChair++;
        if (i == targetFriend) {
            free(arr); free(freeChairs); free(leaving);
            return chair;
        }
        leavePush(leaving, &leaveSz, (Leave){leave, chair});
    }
    free(arr); free(freeChairs); free(leaving);
    return -1;
}
