// LeetCode 1840 - Maximum Building Height
// https://leetcode.com/problems/maximum-building-height/

#include <stdlib.h>

typedef struct {
    int id;
    int height;
} Point;

static int cmpPoint(const void* a, const void* b) {
    const Point* x = (const Point*)a;
    const Point* y = (const Point*)b;
    return (x->id > y->id) - (x->id < y->id);
}

int maxBuilding(int n, int** restrictions, int restrictionsSize, int* restrictionsColSize) {
    (void)restrictionsColSize;
    int count = restrictionsSize + 2;
    Point* points = (Point*)malloc((size_t)count * sizeof(Point));
    points[0].id = 1;
    points[0].height = 0;
    for (int i = 0; i < restrictionsSize; i++) {
        points[i + 1].id = restrictions[i][0];
        points[i + 1].height = restrictions[i][1];
    }
    qsort(points + 1, (size_t)restrictionsSize, sizeof(Point), cmpPoint);

    int used = restrictionsSize + 1;
    if (points[used - 1].id != n) {
        points[used].id = n;
        points[used].height = n - 1;
        used++;
    }

    for (int i = 1; i < used; i++) {
        int limit = points[i - 1].height + points[i].id - points[i - 1].id;
        if (points[i].height > limit) points[i].height = limit;
    }
    for (int i = used - 2; i >= 0; i--) {
        int limit = points[i + 1].height + points[i + 1].id - points[i].id;
        if (points[i].height > limit) points[i].height = limit;
    }

    int best = 0;
    for (int i = 0; i < used; i++) {
        if (points[i].height > best) best = points[i].height;
    }
    for (int i = 0; i < used - 1; i++) {
        int cand = (points[i].height + points[i + 1].height + points[i + 1].id - points[i].id) / 2;
        if (cand > best) best = cand;
    }
    free(points);
    return best;
}
