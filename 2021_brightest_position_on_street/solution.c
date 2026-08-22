// LeetCode 2021 - Brightest Position on Street
// https://leetcode.com/problems/brightest-position-on-street/

#include <stdlib.h>

typedef struct { int x, d; } Ev2021;

static int cmpEv2021(const void* a, const void* b) {
    const Ev2021* ea = a, *eb = b;
    if (ea->x != eb->x) return ea->x < eb->x ? -1 : 1;
    return eb->d - ea->d;
}

int brightestPosition(int** lights, int lightsSize, int* lightsColSize) {
    (void)lightsColSize;
    Ev2021* events = (Ev2021*)malloc((size_t)lightsSize * 2 * sizeof(Ev2021));
    int en = 0;
    for (int i = 0; i < lightsSize; i++) {
        int pos = lights[i][0], r = lights[i][1];
        events[en++] = (Ev2021){pos - r, 1};
        events[en++] = (Ev2021){pos + r + 1, -1};
    }
    qsort(events, (size_t)en, sizeof(Ev2021), cmpEv2021);
    int best = 0, cur = 0, ans = 0;
    for (int i = 0; i < en; i++) {
        cur += events[i].d;
        if (cur > best) { best = cur; ans = events[i].x; }
    }
    free(events);
    return ans;
}
