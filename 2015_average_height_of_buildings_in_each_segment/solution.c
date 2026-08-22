// LeetCode 2015 - Average Height of Buildings in Each Segment
// https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

#include <stdlib.h>

typedef struct { int x, d, h; } Ev2015;

static int cmpEv2015(const void* a, const void* b) {
    const Ev2015* ea = a, *eb = b;
    if (ea->x != eb->x) return ea->x - eb->x;
    return ea->d - eb->d;
}

int** averageHeightOfBuildings(int** buildings, int buildingsSize, int* buildingsColSize, int* returnSize, int** returnColumnSizes) {
    (void)buildingsColSize;
    Ev2015* events = (Ev2015*)malloc((size_t)buildingsSize * 2 * sizeof(Ev2015));
    int en = 0;
    for (int i = 0; i < buildingsSize; i++) {
        events[en++] = (Ev2015){buildings[i][0], 1, buildings[i][2]};
        events[en++] = (Ev2015){buildings[i][1], -1, buildings[i][2]};
    }
    qsort(events, (size_t)en, sizeof(Ev2015), cmpEv2015);
    int** ans = (int**)malloc((size_t)en * sizeof(int*));
    int an = 0;
    int count = 0, sum = 0, prev = events[0].x;
    for (int i = 0; i < en; i++) {
        Ev2015 e = events[i];
        if (e.x != prev && count > 0) {
            int avg = sum / count;
            if (an > 0 && ans[an - 1][1] == prev && ans[an - 1][2] == avg) {
                ans[an - 1][1] = e.x;
            } else {
                ans[an] = (int*)malloc(3 * sizeof(int));
                ans[an][0] = prev; ans[an][1] = e.x; ans[an][2] = avg;
                an++;
            }
        }
        count += e.d;
        sum += e.d * e.h;
        prev = e.x;
    }
    free(events);
    *returnSize = an;
    *returnColumnSizes = (int*)malloc((size_t)an * sizeof(int));
    for (int i = 0; i < an; i++) (*returnColumnSizes)[i] = 3;
    return ans;
}
