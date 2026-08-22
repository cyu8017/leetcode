// LeetCode 2049 - Count Nodes With the Highest Score
// https://leetcode.com/problems/count-nodes-with-the-highest-score/

#include <stdlib.h>

int countHighestScoreNodes(int* parents, int parentsSize) {
    int n = parentsSize;
    int* childCnt = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 1; i < n; i++) childCnt[parents[i]]++;
    int** children = (int**)malloc((size_t)n * sizeof(int*));
    int* pos = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) children[i] = (int*)malloc((size_t)(childCnt[i] ? childCnt[i] : 1) * sizeof(int));
    for (int i = 1; i < n; i++) children[parents[i]][pos[parents[i]]++] = i;
    int* size = (int*)calloc((size_t)n, sizeof(int));
    int* stack = (int*)malloc((size_t)n * sizeof(int));
    int* order = (int*)malloc((size_t)n * sizeof(int));
    int top = 0, on = 0;
    stack[top++] = 0;
    while (top) {
        int u = stack[--top];
        order[on++] = u;
        for (int i = 0; i < childCnt[u]; i++) stack[top++] = children[u][i];
    }
    for (int i = on - 1; i >= 0; i--) {
        int u = order[i];
        size[u] = 1;
        for (int j = 0; j < childCnt[u]; j++) size[u] += size[children[u][j]];
    }
    long long best = 0;
    int ans = 0;
    for (int u = 0; u < n; u++) {
        long long score = 1;
        for (int j = 0; j < childCnt[u]; j++) score *= size[children[u][j]];
        int up = n - size[u];
        if (up > 0) score *= up;
        if (score > best) { best = score; ans = 1; }
        else if (score == best) ans++;
    }
    for (int i = 0; i < n; i++) free(children[i]);
    free(children); free(childCnt); free(pos); free(size); free(stack); free(order);
    return ans;
}
