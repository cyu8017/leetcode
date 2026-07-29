// LeetCode 1926 - Nearest Exit from Entrance in Maze
// https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

#include <stdlib.h>

int nearestExit(char** maze, int mazeSize, int* mazeColSize, int* entrance, int entranceSize) {
    (void)entranceSize;
    int m = mazeSize, n = mazeColSize[0];
    int* qr = (int*)malloc((size_t)m * n * sizeof(int));
    int* qc = (int*)malloc((size_t)m * n * sizeof(int));
    int head = 0, tail = 0;
    qr[tail] = entrance[0];
    qc[tail] = entrance[1];
    tail++;
    maze[entrance[0]][entrance[1]] = '+';
    int steps = 0;
    int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    while (head < tail) {
        int sz = tail - head;
        for (int i = 0; i < sz; i++) {
            int r = qr[head], c = qc[head];
            head++;
            for (int d = 0; d < 4; d++) {
                int nr = r + dirs[d][0], nc = c + dirs[d][1];
                if (nr < 0 || nc < 0 || nr >= m || nc >= n || maze[nr][nc] == '+') continue;
                if (nr == 0 || nc == 0 || nr == m - 1 || nc == n - 1) {
                    free(qr); free(qc);
                    return steps + 1;
                }
                maze[nr][nc] = '+';
                qr[tail] = nr;
                qc[tail] = nc;
                tail++;
            }
        }
        steps++;
    }
    free(qr); free(qc);
    return -1;
}
