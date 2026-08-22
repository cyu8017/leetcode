// LeetCode 2751 - Robot Collisions
// https://leetcode.com/problems/robot-collisions/

#include <stdlib.h>
#include <string.h>

typedef struct { int i, h; char d; } Robot;

static int cmp_idx(const void* a, const void* b, void* positions) {
    int ia = *(const int*)a, ib = *(const int*)b;
    int* pos = (int*)positions;
    return pos[ia] - pos[ib];
}

#if defined(__APPLE__)
static int* g_pos;
static int cmp_apple(const void* a, const void* b) {
    int ia = *(const int*)a, ib = *(const int*)b;
    return g_pos[ia] - g_pos[ib];
}
#endif

int* survivedRobotsHealths(int* positions, int positionsSize, int* healths, int healthsSize, char* directions, int* returnSize) {
    (void)healthsSize;
    int n = positionsSize;
    int* idx = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) idx[i] = i;
#if defined(__APPLE__)
    g_pos = positions;
    qsort(idx, n, sizeof(int), cmp_apple);
#else
    qsort_r(idx, n, sizeof(int), cmp_idx, positions);
#endif
    Robot* stack = (Robot*)malloc(n * sizeof(Robot));
    int top = 0;
    for (int t = 0; t < n; t++) {
        int i = idx[t];
        Robot cur = {i, healths[i], directions[i]};
        while (top > 0 && stack[top - 1].d == 'R' && cur.d == 'L') {
            if (stack[top - 1].h == cur.h) {
                top--;
                cur.h = 0;
                break;
            } else if (stack[top - 1].h > cur.h) {
                stack[top - 1].h--;
                cur.h = 0;
                break;
            } else {
                cur.h--;
                top--;
            }
        }
        if (cur.h > 0) stack[top++] = cur;
    }
    int* alive = (int*)calloc(n, sizeof(int));
    int* has = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < top; i++) {
        alive[stack[i].i] = stack[i].h;
        has[stack[i].i] = 1;
    }
    int* ans = (int*)malloc(n * sizeof(int));
    int sz = 0;
    for (int i = 0; i < n; i++) {
        if (has[i]) ans[sz++] = alive[i];
    }
    free(idx); free(stack); free(alive); free(has);
    *returnSize = sz;
    return ans;
}
