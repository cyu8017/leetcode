// LeetCode 1591 - Strange Printer II
// https://leetcode.com/problems/strange-printer-ii/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool isPrintable(int** targetGrid, int targetGridSize, int* targetGridColSize) {
    int m = targetGridSize, n = targetGridColSize[0];
    int present[61] = {0};
    int r1[61], c1[61], r2[61], c2[61];
    for (int c = 0; c <= 60; c++) {
        r1[c] = c1[c] = 1000000000;
        r2[c] = c2[c] = -1;
    }
    for (int r = 0; r < m; r++) {
        for (int col = 0; col < n; col++) {
            int c = targetGrid[r][col];
            present[c] = 1;
            if (r < r1[c]) r1[c] = r;
            if (col < c1[c]) c1[c] = col;
            if (r > r2[c]) r2[c] = r;
            if (col > c2[c]) c2[c] = col;
        }
    }
    int graph[61][61];
    int indegree[61] = {0};
    memset(graph, 0, sizeof(graph));
    int colorCount = 0;
    for (int c = 1; c <= 60; c++) {
        if (!present[c]) continue;
        colorCount++;
        for (int r = r1[c]; r <= r2[c]; r++) {
            for (int col = c1[c]; col <= c2[c]; col++) {
                int other = targetGrid[r][col];
                if (other != c && !graph[c][other]) {
                    graph[c][other] = 1;
                    indegree[other]++;
                }
            }
        }
    }
    int queue[61], qh = 0, qt = 0;
    for (int c = 1; c <= 60; c++) if (present[c] && indegree[c] == 0) queue[qt++] = c;
    int seen = 0;
    while (qh < qt) {
        int c = queue[qh++];
        seen++;
        for (int nxt = 1; nxt <= 60; nxt++) {
            if (graph[c][nxt]) {
                if (--indegree[nxt] == 0) queue[qt++] = nxt;
            }
        }
    }
    return seen == colorCount;
}
