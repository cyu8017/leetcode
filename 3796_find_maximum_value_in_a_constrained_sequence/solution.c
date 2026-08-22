// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

#include <stdlib.h>
#include <limits.h>

int maxValue(int n, int** restrictions, int restrictionsSize, int* restrictionsColSize, int* diff, int diffSize) {
    (void)restrictionsColSize; (void)diffSize;
    const int infinity = INT_MAX / 4;
    int* bound = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) bound[i] = infinity;
    bound[0] = 0;
    for (int i = 0; i < restrictionsSize; i++) bound[restrictions[i][0]] = restrictions[i][1];
    for (int i = 1; i < n; i++) {
        int cand = bound[i - 1] + diff[i - 1];
        if (cand < bound[i]) bound[i] = cand;
    }
    for (int i = n - 2; i >= 0; i--) {
        int cand = bound[i + 1] + diff[i];
        if (cand < bound[i]) bound[i] = cand;
    }
    int answer = 0;
    for (int i = 0; i < n; i++) if (bound[i] > answer) answer = bound[i];
    free(bound);
    return answer;
}
