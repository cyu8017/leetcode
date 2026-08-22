// LeetCode 3242 - Design Neighbor Sum Service
// https://leetcode.com/problems/design-neighbor-sum-service/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int** grid;
    int n;
    int* pos; /* value -> i*n+j+1, 0 if absent; values 0..n*n-1 */
    int dirs[2][5];
} NeighborSum;

NeighborSum* neighborSumCreate(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    NeighborSum* obj = (NeighborSum*)calloc(1, sizeof(NeighborSum));
    obj->n = gridSize;
    obj->grid = grid;
    int N = gridSize * gridSize;
    obj->pos = (int*)calloc((size_t)(N + 1), sizeof(int));
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridSize; j++) {
            obj->pos[grid[i][j]] = i * gridSize + j + 1;
        }
    }
    int d0[5] = {-1, 0, 1, 0, -1};
    int d1[5] = {-1, 1, 1, -1, -1};
    memcpy(obj->dirs[0], d0, sizeof(d0));
    memcpy(obj->dirs[1], d1, sizeof(d1));
    return obj;
}

static int neighborSumCal(NeighborSum* obj, int value, int k) {
    int p = obj->pos[value] - 1;
    int pi = p / obj->n, pj = p % obj->n;
    int s = 0;
    for (int q = 0; q < 4; q++) {
        int x = pi + obj->dirs[k][q];
        int y = pj + obj->dirs[k][q + 1];
        if (x >= 0 && x < obj->n && y >= 0 && y < obj->n) s += obj->grid[x][y];
    }
    return s;
}

int neighborSumAdjacentSum(NeighborSum* obj, int value) {
    return neighborSumCal(obj, value, 0);
}

int neighborSumDiagonalSum(NeighborSum* obj, int value) {
    return neighborSumCal(obj, value, 1);
}

void neighborSumFree(NeighborSum* obj) {
    if (!obj) return;
    free(obj->pos);
    free(obj);
}
