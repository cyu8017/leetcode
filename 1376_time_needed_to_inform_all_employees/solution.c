// LeetCode 1376 - Time Needed to Inform All Employees
// https://leetcode.com/problems/time-needed-to-inform-all-employees/

#include <stdlib.h>

static int dfs(int u, int** children, int* childSize, int* informTime) {
    int best = 0;
    for (int i = 0; i < childSize[u]; i++) {
        int v = dfs(children[u][i], children, childSize, informTime);
        if (v > best) best = v;
    }
    return informTime[u] + best;
}

int numOfMinutes(int n, int headID, int* manager, int managerSize, int* informTime, int informTimeSize) {
    (void)managerSize; (void)informTimeSize;
    int** children = (int**)malloc(n * sizeof(int*));
    int* childSize = (int*)calloc(n, sizeof(int));
    int* childCap = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++) { childCap[i] = 4; children[i] = (int*)malloc(4 * sizeof(int)); }
    for (int i = 0; i < n; i++) if (manager[i] != -1) {
        int p = manager[i];
        if (childSize[p] == childCap[p]) {
            childCap[p] *= 2;
            children[p] = (int*)realloc(children[p], childCap[p] * sizeof(int));
        }
        children[p][childSize[p]++] = i;
    }
    int ans = dfs(headID, children, childSize, informTime);
    for (int i = 0; i < n; i++) free(children[i]);
    free(children); free(childSize); free(childCap);
    return ans;
}
