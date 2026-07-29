// LeetCode 0773 - Sliding Puzzle
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int slidingPuzzle(int** board, int boardSize, int* boardColSize) {
    (void)boardSize; (void)boardColSize;
    char start[7];
    int p = 0;
    for (int i = 0; i < 2; i++) for (int j = 0; j < 3; j++) start[p++] = (char)('0' + board[i][j]);
    start[6] = '\0';
    const char* target = "123450";
    int neighbors[6][4] = {{1,3,-1,-1},{0,2,4,-1},{1,5,-1,-1},{0,4,-1,-1},{1,3,5,-1},{2,4,-1,-1}};
    char q[800][7];
    int dist[800];
    int head = 0, tail = 0;
    strcpy(q[tail], start); dist[tail++] = 0;
    bool seen[1000000] = {0};
    int key = atoi(start); seen[key] = true;
    while (head < tail) {
        char* state = q[head];
        int steps = dist[head++];
        if (strcmp(state, target) == 0) return steps;
        int zero = 0; while (state[zero] != '0') zero++;
        for (int t = 0; t < 4 && neighbors[zero][t] != -1; t++) {
            int nei = neighbors[zero][t];
            char nxt[7]; strcpy(nxt, state);
            char tmp = nxt[zero]; nxt[zero] = nxt[nei]; nxt[nei] = tmp;
            int k = atoi(nxt);
            if (!seen[k]) { seen[k] = true; strcpy(q[tail], nxt); dist[tail++] = steps + 1; }
        }
    }
    return -1;
}
