// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

#include <stdlib.h>

typedef struct { long long key; long long parent; int size; int used; } UF3873;

static UF3873* uf3873;
static int ufcap3873;

static int uf_slot(long long x, int create) {
    unsigned h = (unsigned)(x ^ (x >> 32)) * 2654435761u;
    int i = (int)(h % (unsigned)ufcap3873);
    for (int t = 0; t < ufcap3873; t++) {
        int j = (i + t) % ufcap3873;
        if (!uf3873[j].used) {
            if (!create) return -1;
            uf3873[j].used = 1; uf3873[j].key = x; uf3873[j].parent = x; uf3873[j].size = 1;
            return j;
        }
        if (uf3873[j].key == x) return j;
    }
    return -1;
}

static long long uf_find(long long x) {
    int j = uf_slot(x, 1);
    if (uf3873[j].parent != x) {
        uf3873[j].parent = uf_find(uf3873[j].parent);
    }
    return uf3873[j].parent;
}

static void uf_union(long long a, long long b) {
    long long pa = uf_find(a), pb = uf_find(b);
    if (pa == pb) return;
    int ia = uf_slot(pa, 0), ib = uf_slot(pb, 0);
    if (uf3873[ia].size > uf3873[ib].size) {
        uf3873[ib].parent = pa;
        uf3873[ia].size += uf3873[ib].size;
    } else {
        uf3873[ia].parent = pb;
        uf3873[ib].size += uf3873[ia].size;
    }
}

int maxActivated(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    ufcap3873 = 1;
    while (ufcap3873 < pointsSize * 8 + 16) ufcap3873 <<= 1;
    uf3873 = (UF3873*)calloc((size_t)ufcap3873, sizeof(UF3873));
    long long m = 3000000000LL;
    for (int i = 0; i < pointsSize; i++) uf_union(points[i][0], points[i][1] + m);
    long long* roots = (long long*)malloc((size_t)pointsSize * sizeof(long long));
    int* cnt = (int*)calloc((size_t)pointsSize, sizeof(int));
    int rsz = 0;
    for (int i = 0; i < pointsSize; i++) {
        long long root = uf_find(points[i][0]);
        int found = -1;
        for (int j = 0; j < rsz; j++) if (roots[j] == root) { found = j; break; }
        if (found < 0) { roots[rsz] = root; cnt[rsz] = 1; rsz++; }
        else cnt[found]++;
    }
    int mx1 = 0, mx2 = 0;
    for (int i = 0; i < rsz; i++) {
        int x = cnt[i];
        if (mx1 < x) { mx2 = mx1; mx1 = x; }
        else if (mx2 < x) mx2 = x;
    }
    free(uf3873); free(roots); free(cnt);
    return mx1 + mx2 + 1;
}
