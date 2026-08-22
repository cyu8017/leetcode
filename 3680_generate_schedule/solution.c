// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

#include <stdlib.h>
#include <string.h>

static int** matches;
static int matchesN;
static int* used;
static int** sched;
static int schedN;
static int last0, last1;
static int nGlob;

static int dfs(void) {
    if (schedN == matchesN) return 1;
    for (int i = 0; i < matchesN; i++) {
        if (used[i]) continue;
        int* m = matches[i];
        if (m[0] == last0 || m[0] == last1 || m[1] == last0 || m[1] == last1) continue;
        used[i] = 1;
        sched[schedN][0] = m[0];
        sched[schedN][1] = m[1];
        schedN++;
        int p0 = last0, p1 = last1;
        last0 = m[0]; last1 = m[1];
        if (dfs()) return 1;
        last0 = p0; last1 = p1;
        schedN--;
        used[i] = 0;
    }
    return 0;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** generateSchedule(int n, int* returnSize, int** returnColumnSizes) {
    if (n < 5) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    nGlob = n;
    matchesN = n * (n - 1);
    matches = (int**)malloc((size_t)matchesN * sizeof(int*));
    int mi = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j) {
                matches[mi] = (int*)malloc(2 * sizeof(int));
                matches[mi][0] = i; matches[mi][1] = j;
                mi++;
            }
        }
    }
    used = (int*)calloc((size_t)matchesN, sizeof(int));
    sched = (int**)malloc((size_t)matchesN * sizeof(int*));
    for (int i = 0; i < matchesN; i++) sched[i] = (int*)malloc(2 * sizeof(int));
    schedN = 0;
    last0 = last1 = -1;
    int ok = dfs();
    if (!ok) {
        for (int i = 0; i < matchesN; i++) { free(matches[i]); free(sched[i]); }
        free(matches); free(sched); free(used);
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    int** result = (int**)malloc((size_t)schedN * sizeof(int*));
    int* cols = (int*)malloc((size_t)schedN * sizeof(int));
    for (int i = 0; i < schedN; i++) {
        result[i] = (int*)malloc(2 * sizeof(int));
        result[i][0] = sched[i][0];
        result[i][1] = sched[i][1];
        cols[i] = 2;
    }
    *returnSize = schedN;
    *returnColumnSizes = cols;
    for (int i = 0; i < matchesN; i++) { free(matches[i]); free(sched[i]); }
    free(matches); free(sched); free(used);
    return result;
}
