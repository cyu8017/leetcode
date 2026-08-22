// LeetCode 2069 - Walking Robot Simulation II
// https://leetcode.com/problems/walking-robot-simulation-ii/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    int w, h, peri, pos;
    bool moved;
} Robot;

Robot* robotCreate(int width, int height) {
    Robot* obj = (Robot*)calloc(1, sizeof(Robot));
    obj->w = width; obj->h = height;
    obj->peri = 2 * (width + height) - 4;
    return obj;
}

void robotStep(Robot* obj, int num) {
    obj->moved = true;
    obj->pos = (obj->pos + num) % obj->peri;
}

static void getPosDir2069(Robot* obj, int* x, int* y, char** dir) {
    int p = obj->pos, w = obj->w, h = obj->h;
    if (p == 0) {
        *x = 0; *y = 0;
        *dir = obj->moved ? "South" : "East";
        return;
    }
    if (p <= w - 1) { *x = p; *y = 0; *dir = "East"; return; }
    p -= w - 1;
    if (p <= h - 1) { *x = w - 1; *y = p; *dir = "North"; return; }
    p -= h - 1;
    if (p <= w - 1) { *x = w - 1 - p; *y = h - 1; *dir = "West"; return; }
    p -= w - 1;
    *x = 0; *y = h - 1 - p; *dir = "South";
}

int* robotGetPos(Robot* obj, int* retSize) {
    int x, y; char* d;
    getPosDir2069(obj, &x, &y, &d);
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = x; ans[1] = y;
    *retSize = 2;
    return ans;
}

char* robotGetDir(Robot* obj) {
    int x, y; char* d;
    getPosDir2069(obj, &x, &y, &d);
    return d;
}

void robotFree(Robot* obj) { free(obj); }
