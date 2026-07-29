// LeetCode 0909 - Snakes and Ladders
// https://leetcode.com/problems/snakes-and-ladders/

#include <stdlib.h>
#include <string.h>

static void pos(int square, int n, int* r, int* c) {
    square--;
    int row = square / n;
    int rem = square % n;
    *r = n - 1 - row;
    *c = (row % 2 == 0) ? rem : n - 1 - rem;
}

int snakesAndLadders(int** board, int boardSize, int* boardColSize) {
    (void)boardColSize;
    int n = boardSize;
    int target = n * n;
    int* queue = (int*)malloc((size_t)(target + 1) * sizeof(int));
    char* seen = (char*)calloc((size_t)(target + 1), 1);
    int head = 0, tail = 0;
    queue[tail++] = 1;
    seen[1] = 1;
    int moves = 0;
    while (head < tail) {
        int sz = tail - head;
        for (int s = 0; s < sz; s++) {
            int cur = queue[head++];
            if (cur == target) {
                free(queue); free(seen);
                return moves;
            }
            int lim = cur + 6 < target ? cur + 6 : target;
            for (int nxt = cur + 1; nxt <= lim; nxt++) {
                int r, c;
                pos(nxt, n, &r, &c);
                int dest = board[r][c] != -1 ? board[r][c] : nxt;
                if (!seen[dest]) {
                    seen[dest] = 1;
                    queue[tail++] = dest;
                }
            }
        }
        moves++;
    }
    free(queue); free(seen);
    return -1;
}
