// LeetCode 2013 - Detect Squares
// https://leetcode.com/problems/detect-squares/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int x, y, cnt;
    int used;
} DSEntry;

typedef struct {
    DSEntry* tab;
    int cap;
    int size;
} DetectSquares;

static unsigned hashXY(int x, int y) {
    return (unsigned)x * 2654435761u ^ (unsigned)y * 40503u;
}

static void dsEnsure(DetectSquares* obj) {
    if (obj->size * 2 < obj->cap) return;
    int oldCap = obj->cap;
    DSEntry* old = obj->tab;
    obj->cap *= 2;
    obj->tab = (DSEntry*)calloc((size_t)obj->cap, sizeof(DSEntry));
    obj->size = 0;
    for (int i = 0; i < oldCap; i++) {
        if (!old[i].used) continue;
        unsigned h = hashXY(old[i].x, old[i].y);
        int idx = (int)(h & (unsigned)(obj->cap - 1));
        while (obj->tab[idx].used) idx = (idx + 1) & (obj->cap - 1);
        obj->tab[idx] = old[i];
        obj->size++;
    }
    free(old);
}

static int* dsFind(DetectSquares* obj, int x, int y, int create) {
    unsigned h = hashXY(x, y);
    int idx = (int)(h & (unsigned)(obj->cap - 1));
    for (;;) {
        if (!obj->tab[idx].used) {
            if (!create) return NULL;
            obj->tab[idx].used = 1;
            obj->tab[idx].x = x;
            obj->tab[idx].y = y;
            obj->tab[idx].cnt = 0;
            obj->size++;
            return &obj->tab[idx].cnt;
        }
        if (obj->tab[idx].x == x && obj->tab[idx].y == y) return &obj->tab[idx].cnt;
        idx = (idx + 1) & (obj->cap - 1);
    }
}

static int dsGet(DetectSquares* obj, int x, int y) {
    int* p = dsFind(obj, x, y, 0);
    return p ? *p : 0;
}

DetectSquares* detectSquaresCreate(void) {
    DetectSquares* obj = (DetectSquares*)calloc(1, sizeof(DetectSquares));
    obj->cap = 1024;
    obj->tab = (DSEntry*)calloc((size_t)obj->cap, sizeof(DSEntry));
    return obj;
}

void detectSquaresAdd(DetectSquares* obj, int* point, int pointSize) {
    (void)pointSize;
    dsEnsure(obj);
    (*dsFind(obj, point[0], point[1], 1))++;
}

int detectSquaresCount(DetectSquares* obj, int* point, int pointSize) {
    (void)pointSize;
    int x = point[0], y = point[1], ans = 0;
    for (int i = 0; i < obj->cap; i++) {
        if (!obj->tab[i].used) continue;
        int px = obj->tab[i].x, py = obj->tab[i].y, c = obj->tab[i].cnt;
        if (px == x || py == y) continue;
        int dx = px - x; if (dx < 0) dx = -dx;
        int dy = py - y; if (dy < 0) dy = -dy;
        if (dx != dy) continue;
        ans += c * dsGet(obj, px, y) * dsGet(obj, x, py);
    }
    return ans;
}

void detectSquaresFree(DetectSquares* obj) {
    if (!obj) return;
    free(obj->tab);
    free(obj);
}
