// LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
// https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int minimumOperationsToMakeEqual(int x, int y) {
    if (x <= y) return y - x;
    int limit = 2 * x + 20;
    bool* seen = (bool*)calloc((size_t)(limit + 1), sizeof(bool));
    int* qv = (int*)malloc((size_t)(limit + 1) * sizeof(int));
    int* qd = (int*)malloc((size_t)(limit + 1) * sizeof(int));
    int head = 0, tail = 0;
    qv[tail] = x;
    qd[tail] = 0;
    tail++;
    seen[x] = true;
    while (head < tail) {
        int cur = qv[head];
        int d = qd[head];
        head++;
        if (cur == y) {
            free(seen); free(qv); free(qd);
            return d;
        }
        int cands[4];
        int cn = 0;
        cands[cn++] = cur + 1;
        cands[cn++] = cur - 1;
        if (cur % 11 == 0) cands[cn++] = cur / 11;
        if (cur % 5 == 0) cands[cn++] = cur / 5;
        for (int i = 0; i < cn; i++) {
            int nxt = cands[i];
            if (nxt > 0 && nxt <= limit && !seen[nxt]) {
                seen[nxt] = true;
                qv[tail] = nxt;
                qd[tail] = d + 1;
                tail++;
            }
        }
    }
    free(seen); free(qv); free(qd);
    return -1;
}
