// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int br, bc, pr, pc;
} State;

static int reachable(char** grid, int m, int n, int sr, int sc, int br, int bc, int* out, int outCap) {
    int* stackR = (int*)malloc((size_t)(m * n) * sizeof(int));
    int* stackC = (int*)malloc((size_t)(m * n) * sizeof(int));
    int* seen = (int*)calloc((size_t)(m * n), sizeof(int));
    int top = 0, count = 0;
    stackR[top] = sr;
    stackC[top] = sc;
    top++;
    seen[sr * n + sc] = 1;
    while (top > 0) {
        int r = stackR[--top];
        int c = stackC[top];
        if (count < outCap) out[count++] = r * n + c;
        static const int dr[4] = {1, -1, 0, 0};
        static const int dc[4] = {0, 0, 1, -1};
        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k], nc = c + dc[k];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            if (grid[nr][nc] == '#') continue;
            if (nr == br && nc == bc) continue;
            if (seen[nr * n + nc]) continue;
            seen[nr * n + nc] = 1;
            stackR[top] = nr;
            stackC[top] = nc;
            top++;
        }
    }
    free(stackR);
    free(stackC);
    free(seen);
    return count;
}

int minPushBox(char** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int br = 0, bc = 0, pr = 0, pc = 0, tr = 0, tc = 0;
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (grid[r][c] == 'B') { br = r; bc = c; }
            else if (grid[r][c] == 'S') { pr = r; pc = c; }
            else if (grid[r][c] == 'T') { tr = r; tc = c; }
        }
    }
    int maxStates = m * n * m * n;
    State* queue = (State*)malloc((size_t)maxStates * sizeof(State));
    int* dist = (int*)malloc((size_t)maxStates * sizeof(int));
    int* seen = (int*)calloc((size_t)maxStates, sizeof(int));
    int head = 0, tail = 0;
    int startIdx = ((br * n + bc) * (m * n)) + (pr * n + pc);
    queue[tail++] = (State){br, bc, pr, pc};
    dist[startIdx] = 0;
    seen[startIdx] = 1;
    int* reach = (int*)malloc((size_t)(m * n) * sizeof(int));
    static const int dr[4] = {1, -1, 0, 0};
    static const int dc[4] = {0, 0, 1, -1};
    while (head < tail) {
        State cur = queue[head++];
        if (cur.br == tr && cur.bc == tc) {
            int ans = dist[((cur.br * n + cur.bc) * (m * n)) + (cur.pr * n + cur.pc)];
            free(queue);
            free(dist);
            free(seen);
            free(reach);
            return ans;
        }
        int reachCount = reachable(grid, m, n, cur.pr, cur.pc, cur.br, cur.bc, reach, m * n);
        for (int d = 0; d < 4; d++) {
            int standR = cur.br - dr[d], standC = cur.bc - dc[d];
            int nbr = cur.br + dr[d], nbc = cur.bc + dc[d];
            if (nbr < 0 || nbr >= m || nbc < 0 || nbc >= n) continue;
            if (grid[nbr][nbc] == '#') continue;
            int ok = 0;
            int stand = standR * n + standC;
            for (int i = 0; i < reachCount; i++) if (reach[i] == stand) { ok = 1; break; }
            if (!ok) continue;
            int idx = ((nbr * n + nbc) * (m * n)) + (cur.br * n + cur.bc);
            if (seen[idx]) continue;
            seen[idx] = 1;
            dist[idx] = dist[((cur.br * n + cur.bc) * (m * n)) + (cur.pr * n + cur.pc)] + 1;
            queue[tail++] = (State){nbr, nbc, cur.br, cur.bc};
        }
    }
    free(queue);
    free(dist);
    free(seen);
    free(reach);
    return -1;
}
