// LeetCode 3568 - Minimum Moves to Clean the Classroom
// https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { int i, j, e, mask; } State;

int minMoves(char** classroom, int classroomSize, int energy) {
    int m = classroomSize, n = (int)strlen(classroom[0]);
    int** d = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) d[i] = (int*)calloc((size_t)n, sizeof(int));
    int x = 0, y = 0, cnt = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            char c = classroom[i][j];
            if (c == 'S') { x = i; y = j; }
            else if (c == 'L') { d[i][j] = cnt++; }
        }
    }
    if (cnt == 0) {
        for (int i = 0; i < m; i++) free(d[i]);
        free(d);
        return 0;
    }
    int masks = 1 << cnt;
    bool**** vis = (bool****)malloc((size_t)m * sizeof(bool***));
    for (int i = 0; i < m; i++) {
        vis[i] = (bool***)malloc((size_t)n * sizeof(bool**));
        for (int j = 0; j < n; j++) {
            vis[i][j] = (bool**)malloc((size_t)(energy + 1) * sizeof(bool*));
            for (int e = 0; e <= energy; e++)
                vis[i][j][e] = (bool*)calloc((size_t)masks, sizeof(bool));
        }
    }
    State* q = (State*)malloc(sizeof(State) * 2000000);
    int qh = 0, qt = 0;
    int startMask = masks - 1;
    q[qt++] = (State){x, y, energy, startMask};
    vis[x][y][energy][startMask] = true;
    int dirs[5] = {-1, 0, 1, 0, -1};
    int ans = 0;
    while (qh < qt) {
        int sz = qt - qh;
        for (int s = 0; s < sz; s++) {
            State cur = q[qh++];
            if (cur.mask == 0) {
                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < n; j++) {
                        for (int e = 0; e <= energy; e++) free(vis[i][j][e]);
                        free(vis[i][j]);
                    }
                    free(vis[i]); free(d[i]);
                }
                free(vis); free(d); free(q);
                return ans;
            }
            if (cur.e <= 0) continue;
            for (int k = 0; k < 4; k++) {
                int nx = cur.i + dirs[k], ny = cur.j + dirs[k + 1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && classroom[nx][ny] != 'X') {
                    int nxtE = classroom[nx][ny] == 'R' ? energy : cur.e - 1;
                    int nxtMask = cur.mask;
                    if (classroom[nx][ny] == 'L') nxtMask &= ~(1 << d[nx][ny]);
                    if (!vis[nx][ny][nxtE][nxtMask]) {
                        vis[nx][ny][nxtE][nxtMask] = true;
                        q[qt++] = (State){nx, ny, nxtE, nxtMask};
                    }
                }
            }
        }
        ans++;
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            for (int e = 0; e <= energy; e++) free(vis[i][j][e]);
            free(vis[i][j]);
        }
        free(vis[i]); free(d[i]);
    }
    free(vis); free(d); free(q);
    return -1;
}
