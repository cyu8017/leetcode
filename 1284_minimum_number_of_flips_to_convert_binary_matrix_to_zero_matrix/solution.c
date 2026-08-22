// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

#include <stdlib.h>

typedef struct {
    int state;
    int dist;
} Node;

int minFlips(int** mat, int matSize, int* matColSize) {
    int m = matSize, n = matColSize[0];
    int total = m * n;
    int start = 0;
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (mat[r][c]) start |= 1 << (r * n + c);
        }
    }
    int maskCount = total;
    int* masks = (int*)malloc((size_t)maskCount * sizeof(int));
    int idx = 0;
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            int mask = 0;
            for (int dr = -1; dr <= 1; dr++) {
                for (int dc = -1; dc <= 1; dc++) {
                    if (dr == 0 && dc == 0) continue;
                    if (dr != 0 && dc != 0) continue;
                    int nr = r + dr, nc = c + dc;
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n) mask |= 1 << (nr * n + nc);
                }
            }
            mask |= 1 << (r * n + c);
            masks[idx++] = mask;
        }
    }
    int maxState = 1 << total;
    int* dist = (int*)malloc((size_t)maxState * sizeof(int));
    for (int i = 0; i < maxState; i++) dist[i] = -1;
    Node* queue = (Node*)malloc((size_t)maxState * sizeof(Node));
    int head = 0, tail = 0;
    queue[tail++] = (Node){start, 0};
    dist[start] = 0;
    while (head < tail) {
        Node cur = queue[head++];
        if (cur.state == 0) {
            int ans = cur.dist;
            free(masks);
            free(dist);
            free(queue);
            return ans;
        }
        for (int i = 0; i < maskCount; i++) {
            int nxt = cur.state ^ masks[i];
            if (dist[nxt] == -1) {
                dist[nxt] = cur.dist + 1;
                queue[tail++] = (Node){nxt, cur.dist + 1};
            }
        }
    }
    free(masks);
    free(dist);
    free(queue);
    return -1;
}
