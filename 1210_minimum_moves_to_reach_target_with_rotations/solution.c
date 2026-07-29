// LeetCode 1210 - Minimum Moves to Reach Target with Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int r, c, orient;
} State;

int minimumMoves(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize;
    State target = {n - 1, n - 2, 0};
    int cap = n * n * 2;
    char* seen = (char*)calloc((size_t)cap, 1);
    State* queue = (State*)malloc((size_t)cap * sizeof(State));
    int* dist = (int*)malloc((size_t)cap * sizeof(int));
    int qs = 0, qe = 0;
    State start = {0, 0, 0};
    queue[qe] = start;
    dist[qe] = 0;
    qe++;
    seen[0] = 1;
    while (qs < qe) {
        State cur = queue[qs];
        int moves = dist[qs++];
        if (cur.r == target.r && cur.c == target.c && cur.orient == target.orient) {
            free(seen);
            free(queue);
            free(dist);
            return moves;
        }
        State next[4];
        int nextCount = 0;
        if (cur.orient == 0) {
            if (cur.c + 2 < n && grid[cur.r][cur.c + 2] == 0) {
                next[nextCount++] = (State){cur.r, cur.c + 1, 0};
            }
            if (cur.r + 1 < n && grid[cur.r + 1][cur.c] == 0 && grid[cur.r + 1][cur.c + 1] == 0) {
                next[nextCount++] = (State){cur.r + 1, cur.c, 0};
                next[nextCount++] = (State){cur.r, cur.c, 1};
            }
        } else {
            if (cur.r + 2 < n && grid[cur.r + 2][cur.c] == 0) {
                next[nextCount++] = (State){cur.r + 1, cur.c, 1};
            }
            if (cur.c + 1 < n && grid[cur.r][cur.c + 1] == 0 && grid[cur.r + 1][cur.c + 1] == 0) {
                next[nextCount++] = (State){cur.r, cur.c + 1, 1};
                next[nextCount++] = (State){cur.r, cur.c, 0};
            }
        }
        for (int i = 0; i < nextCount; i++) {
            int key = (next[i].r * n + next[i].c) * 2 + next[i].orient;
            if (!seen[key]) {
                seen[key] = 1;
                queue[qe] = next[i];
                dist[qe] = moves + 1;
                qe++;
            }
        }
    }
    free(seen);
    free(queue);
    free(dist);
    return -1;
}
