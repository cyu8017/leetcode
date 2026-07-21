// LeetCode 1882 - Process Tasks Using Servers
// https://leetcode.com/problems/process-tasks-using-servers/

#include <stdlib.h>

typedef struct {
    int weight;
    int index;
} Avail;

typedef struct {
    long long finish;
    int weight;
    int index;
} Busy;

static void swapAvail(Avail* a, Avail* b) {
    Avail t = *a;
    *a = *b;
    *b = t;
}

static void swapBusy(Busy* a, Busy* b) {
    Busy t = *a;
    *a = *b;
    *b = t;
}

static int availLess(Avail a, Avail b) {
    if (a.weight != b.weight) return a.weight < b.weight;
    return a.index < b.index;
}

static int busyLess(Busy a, Busy b) {
    if (a.finish != b.finish) return a.finish < b.finish;
    if (a.weight != b.weight) return a.weight < b.weight;
    return a.index < b.index;
}

static void availPush(Avail* h, int* sz, Avail v) {
    int i = (*sz)++;
    h[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (!availLess(h[i], h[p])) break;
        swapAvail(&h[i], &h[p]);
        i = p;
    }
}

static Avail availPop(Avail* h, int* sz) {
    Avail top = h[0];
    h[0] = h[--(*sz)];
    int i = 0;
    while (1) {
        int l = i * 2 + 1, r = i * 2 + 2, best = i;
        if (l < *sz && availLess(h[l], h[best])) best = l;
        if (r < *sz && availLess(h[r], h[best])) best = r;
        if (best == i) break;
        swapAvail(&h[i], &h[best]);
        i = best;
    }
    return top;
}

static void busyPush(Busy* h, int* sz, Busy v) {
    int i = (*sz)++;
    h[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (!busyLess(h[i], h[p])) break;
        swapBusy(&h[i], &h[p]);
        i = p;
    }
}

static Busy busyPop(Busy* h, int* sz) {
    Busy top = h[0];
    h[0] = h[--(*sz)];
    int i = 0;
    while (1) {
        int l = i * 2 + 1, r = i * 2 + 2, best = i;
        if (l < *sz && busyLess(h[l], h[best])) best = l;
        if (r < *sz && busyLess(h[r], h[best])) best = r;
        if (best == i) break;
        swapBusy(&h[i], &h[best]);
        i = best;
    }
    return top;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* assignTasks(int* servers, int serversSize, int* tasks, int tasksSize, int* returnSize) {
    Avail* available = (Avail*)malloc((size_t)serversSize * sizeof(Avail));
    Busy* busy = (Busy*)malloc((size_t)serversSize * sizeof(Busy));
    int availSize = 0, busySize = 0;
    for (int i = 0; i < serversSize; i++) {
        Avail a = {servers[i], i};
        availPush(available, &availSize, a);
    }
    int* answer = (int*)malloc((size_t)tasksSize * sizeof(int));
    long long time = 0;
    for (int moment = 0; moment < tasksSize; moment++) {
        if (time < moment) time = moment;
        while (busySize > 0 && busy[0].finish <= time) {
            Busy b = busyPop(busy, &busySize);
            Avail a = {b.weight, b.index};
            availPush(available, &availSize, a);
        }
        while (availSize == 0) {
            time = busy[0].finish;
            while (busySize > 0 && busy[0].finish <= time) {
                Busy b = busyPop(busy, &busySize);
                Avail a = {b.weight, b.index};
                availPush(available, &availSize, a);
            }
        }
        Avail chosen = availPop(available, &availSize);
        Busy b = {time + tasks[moment], chosen.weight, chosen.index};
        busyPush(busy, &busySize, b);
        answer[moment] = chosen.index;
    }
    free(available);
    free(busy);
    *returnSize = tasksSize;
    return answer;
}
