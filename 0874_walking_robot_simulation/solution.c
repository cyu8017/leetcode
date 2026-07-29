// LeetCode 0874 - Walking Robot Simulation
// https://leetcode.com/problems/walking-robot-simulation/

#include <stdlib.h>
#include <stdbool.h>

#define MAX(a,b) ((a)>(b)?(a):(b))

typedef struct { int x, y; } Pt;

static int cmp_pt(const void* a, const void* b) {
    const Pt* p = a; const Pt* q = b;
    if (p->x != q->x) return p->x - q->x;
    return p->y - q->y;
}

static bool blocked(Pt* obs, int n, int x, int y) {
    Pt key = {x, y};
    return bsearch(&key, obs, (size_t)n, sizeof(Pt), cmp_pt) != NULL;
}

int robotSim(int* commands, int commandsSize, int** obstacles, int obstaclesSize, int* obstaclesColSize) {
    (void)obstaclesColSize;
    Pt* obs = (Pt*)malloc((size_t)(obstaclesSize ? obstaclesSize : 1) * sizeof(Pt));
    for (int i = 0; i < obstaclesSize; i++) obs[i] = (Pt){obstacles[i][0], obstacles[i][1]};
    if (obstaclesSize) qsort(obs, (size_t)obstaclesSize, sizeof(Pt), cmp_pt);
    int dirs[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    int x = 0, y = 0, d = 0, best = 0;
    for (int i = 0; i < commandsSize; i++) {
        int cmd = commands[i];
        if (cmd == -1) d = (d + 1) % 4;
        else if (cmd == -2) d = (d + 3) % 4;
        else {
            for (int s = 0; s < cmd; s++) {
                int nx = x + dirs[d][0], ny = y + dirs[d][1];
                if (obstaclesSize && blocked(obs, obstaclesSize, nx, ny)) break;
                x = nx; y = ny;
            }
            best = MAX(best, x * x + y * y);
        }
    }
    free(obs);
    return best;
}
