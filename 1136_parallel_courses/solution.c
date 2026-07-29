// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

#include <stdlib.h>

int minimumSemesters(int n, int** relations, int relationsSize, int* relationsColSize) {
    (void)relationsColSize;
    int* head = (int*)malloc((size_t)(n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) head[i] = -1;
    int* to = (int*)malloc((size_t)(relationsSize + 1) * sizeof(int));
    int* next = (int*)malloc((size_t)(relationsSize + 1) * sizeof(int));
    int* indeg = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < relationsSize; i++) {
        int u = relations[i][0], v = relations[i][1];
        to[i] = v; next[i] = head[u]; head[u] = i;
        indeg[v]++;
    }
    int* q = (int*)malloc((size_t)(n + 1) * sizeof(int));
    int qs = 0, qe = 0;
    for (int i = 1; i <= n; i++) if (indeg[i] == 0) q[qe++] = i;
    int semesters = 0, taken = 0;
    while (qs < qe) {
        semesters++;
        int sz = qe - qs;
        for (int k = 0; k < sz; k++) {
            int course = q[qs++];
            taken++;
            for (int e = head[course]; e != -1; e = next[e]) {
                int nxt = to[e];
                if (--indeg[nxt] == 0) q[qe++] = nxt;
            }
        }
    }
    free(head); free(to); free(next); free(indeg); free(q);
    return taken == n ? semesters : -1;
}
