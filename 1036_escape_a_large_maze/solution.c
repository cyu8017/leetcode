// LeetCode 1036 - Escape a Large Maze
// https://leetcode.com/problems/escape-a-large-maze/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define GRID 1000000

typedef struct {
    long long key;
    int used;
} SetEnt;

static unsigned hll(long long key, int cap) {
    unsigned long long x = (unsigned long long)key;
    x ^= x >> 33;
    x *= 0xff51afd7ed558ccdULL;
    x ^= x >> 33;
    return (unsigned)(x % (unsigned)cap);
}

static long long pk(int r, int c) {
    return ((long long)r << 32) | (unsigned)c;
}

static void set_put(SetEnt* t, int cap, long long key) {
    unsigned h = hll(key, cap);
    while (t[h].used && t[h].key != key) h = (h + 1) % (unsigned)cap;
    t[h].used = 1;
    t[h].key = key;
}

static int set_find(SetEnt* t, int cap, long long key) {
    unsigned h = hll(key, cap);
    while (t[h].used) {
        if (t[h].key == key) return 1;
        h = (h + 1) % (unsigned)cap;
    }
    return 0;
}

static bool bfs_escape(SetEnt* blocked, int bcap, int* start, int* goal, int limit) {
    int qcap = limit + 5;
    int* qr = (int*)malloc((size_t)qcap * sizeof(int));
    int* qc = (int*)malloc((size_t)qcap * sizeof(int));
    SetEnt* seen = (SetEnt*)calloc((size_t)(qcap * 4 + 64), sizeof(SetEnt));
    int scap = qcap * 4 + 64;
    int head = 0, tail = 0, seenCount = 0;
    qr[tail] = start[0]; qc[tail] = start[1]; tail++;
    set_put(seen, scap, pk(start[0], start[1]));
    seenCount = 1;
    int dr[4] = {1, -1, 0, 0}, dc[4] = {0, 0, 1, -1};
    while (head < tail) {
        if (seenCount > limit) {
            free(qr); free(qc); free(seen);
            return true;
        }
        int r = qr[head], c = qc[head]; head++;
        if (r == goal[0] && c == goal[1]) {
            free(qr); free(qc); free(seen);
            return true;
        }
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr < 0 || nr >= GRID || nc < 0 || nc >= GRID) continue;
            long long key = pk(nr, nc);
            if (set_find(blocked, bcap, key) || set_find(seen, scap, key)) continue;
            set_put(seen, scap, key);
            seenCount++;
            if (tail == qcap) {
                qcap *= 2;
                qr = (int*)realloc(qr, (size_t)qcap * sizeof(int));
                qc = (int*)realloc(qc, (size_t)qcap * sizeof(int));
            }
            qr[tail] = nr; qc[tail] = nc; tail++;
        }
    }
    free(qr); free(qc); free(seen);
    return false;
}

bool isEscapePossible(int** blocked, int blockedSize, int* blockedColSize,
                      int* source, int sourceSize, int* target, int targetSize) {
    (void)blockedColSize; (void)sourceSize; (void)targetSize;
    int bcap = blockedSize * 4 + 64;
    if (bcap < 64) bcap = 64;
    SetEnt* bset = (SetEnt*)calloc((size_t)bcap, sizeof(SetEnt));
    for (int i = 0; i < blockedSize; i++)
        set_put(bset, bcap, pk(blocked[i][0], blocked[i][1]));
    int limit = blockedSize * (blockedSize - 1) / 2;
    bool ok = bfs_escape(bset, bcap, source, target, limit) &&
              bfs_escape(bset, bcap, target, source, limit);
    free(bset);
    return ok;
}
