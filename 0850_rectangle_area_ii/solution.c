// LeetCode 0850 - Rectangle Area II
// https://leetcode.com/problems/rectangle-area-ii/

#include <stdlib.h>

#define MOD 1000000007
#define MAX(a,b) ((a)>(b)?(a):(b))

typedef struct { int x, typ, y1, y2; } Event;
typedef struct { int y1, y2; } Seg;

static int cmp_event(const void* a, const void* b) {
    return ((const Event*)a)->x - ((const Event*)b)->x;
}
static int cmp_seg(const void* a, const void* b) {
    return ((const Seg*)a)->y1 - ((const Seg*)b)->y1;
}

static long long covered_length(Seg* active, int na) {
    if (na == 0) return 0;
    qsort(active, (size_t)na, sizeof(Seg), cmp_seg);
    long long total = 0;
    int cur_start = active[0].y1, cur_end = active[0].y2;
    for (int i = 1; i < na; i++) {
        if (active[i].y1 > cur_end) {
            total += cur_end - cur_start;
            cur_start = active[i].y1;
            cur_end = active[i].y2;
        } else cur_end = MAX(cur_end, active[i].y2);
    }
    total += cur_end - cur_start;
    return total;
}

int rectangleArea(int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    (void)rectanglesColSize;
    Event* events = (Event*)malloc((size_t)rectanglesSize * 2 * sizeof(Event));
    int ne = 0;
    for (int i = 0; i < rectanglesSize; i++) {
        events[ne++] = (Event){rectangles[i][0], 1, rectangles[i][1], rectangles[i][3]};
        events[ne++] = (Event){rectangles[i][2], -1, rectangles[i][1], rectangles[i][3]};
    }
    qsort(events, (size_t)ne, sizeof(Event), cmp_event);
    Seg* active = (Seg*)malloc((size_t)rectanglesSize * sizeof(Seg));
    int na = 0;
    long long area = 0;
    int prev_x = events[0].x;
    for (int i = 0; i < ne; i++) {
        area += covered_length(active, na) * (events[i].x - prev_x);
        if (events[i].typ == 1) {
            active[na++] = (Seg){events[i].y1, events[i].y2};
        } else {
            for (int j = 0; j < na; j++) {
                if (active[j].y1 == events[i].y1 && active[j].y2 == events[i].y2) {
                    active[j] = active[--na];
                    break;
                }
            }
        }
        prev_x = events[i].x;
    }
    free(events); free(active);
    return (int)(area % MOD);
}
