// LeetCode 2805 - Custom Interval
// https://leetcode.com/problems/custom-interval/
// JS timer API; C stand-in stores cancel flag without threading.

#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    void (*fn)(void);
    int delay;
    int period;
    bool cancelled;
} CustomInterval;

CustomInterval* customIntervalCreate(void (*fn)(void), int delay, int period) {
    CustomInterval* c = (CustomInterval*)malloc(sizeof(CustomInterval));
    c->fn = fn;
    c->delay = delay;
    c->period = period;
    c->cancelled = false;
    return c;
}

void customIntervalCancel(CustomInterval* c) {
    if (c) c->cancelled = true;
}

void customIntervalFree(CustomInterval* c) {
    free(c);
}
