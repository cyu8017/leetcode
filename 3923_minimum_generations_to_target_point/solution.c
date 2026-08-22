// LeetCode 3923 - Minimum Generations to Target Point
// https://leetcode.com/problems/minimum-generations-to-target-point/

#include <stdlib.h>
#include <string.h>

typedef struct { int a, b, c; } Pt3923;

static int ptEq3923(Pt3923 x, Pt3923 y) {
    return x.a == y.a && x.b == y.b && x.c == y.c;
}

/* open addressing map Pt -> generation */
enum { HS3923 = 4096 };
typedef struct { Pt3923 key; int val; int used; } Ent3923;
static Ent3923 map3923[HS3923];

static unsigned hash3923(Pt3923 p) {
    return (unsigned)(p.a * 73856093 ^ p.b * 19349663 ^ p.c * 83492791) % HS3923;
}
static int mapGet3923(Pt3923 p, int* found) {
    unsigned h = hash3923(p);
    for (int i = 0; i < HS3923; i++) {
        unsigned j = (h + i) % HS3923;
        if (!map3923[j].used) { *found = 0; return (int)j; }
        if (ptEq3923(map3923[j].key, p)) { *found = 1; return (int)j; }
    }
    *found = 0; return 0;
}
static void mapPut3923(Pt3923 p, int v) {
    int found; int slot = mapGet3923(p, &found);
    map3923[slot].used = 1; map3923[slot].key = p; map3923[slot].val = v;
}

int minGenerations(int** points, int pointsSize, int* pointsColSize, int* target, int targetSize) {
    (void)pointsColSize; (void)targetSize;
    memset(map3923, 0, sizeof(map3923));
    Pt3923 targetPoint = {target[0], target[1], target[2]};
    Pt3923* all = malloc(1024 * sizeof(Pt3923));
    int an = 0, acap = 1024;
    for (int i = 0; i < pointsSize; i++) {
        Pt3923 p = {points[i][0], points[i][1], points[i][2]};
        mapPut3923(p, 0);
        if (an == acap) { acap *= 2; all = realloc(all, (size_t)acap * sizeof(Pt3923)); }
        all[an++] = p;
    }
    int found;
    int slot = mapGet3923(targetPoint, &found);
    if (found) { free(all); return map3923[slot].val; }

    for (int current = 1; ; current++) {
        int limit = an;
        Pt3923* added = malloc((size_t)(limit * limit + 1) * sizeof(Pt3923));
        int addn = 0;
        for (int i = 0; i < limit; i++) {
            for (int j = i + 1; j < limit; j++) {
                if (ptEq3923(all[i], all[j])) continue;
                Pt3923 p = {
                    (all[i].a + all[j].a) / 2,
                    (all[i].b + all[j].b) / 2,
                    (all[i].c + all[j].c) / 2
                };
                int f; mapGet3923(p, &f);
                if (!f) {
                    mapPut3923(p, current);
                    added[addn++] = p;
                }
            }
        }
        slot = mapGet3923(targetPoint, &found);
        if (found) {
            int v = map3923[slot].val;
            free(added); free(all);
            return v;
        }
        if (addn == 0) { free(added); free(all); return -1; }
        while (an + addn > acap) { acap *= 2; all = realloc(all, (size_t)acap * sizeof(Pt3923)); }
        memcpy(all + an, added, (size_t)addn * sizeof(Pt3923));
        an += addn;
        free(added);
    }
}
