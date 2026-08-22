// LeetCode 3447 - Assign Elements to Groups With Constraints
// https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

#include <stdlib.h>

int* assignElements(int* groups, int groupsSize, int* elements, int elementsSize, int* returnSize) {
    const int maxV = 100001;
    int* first = (int*)malloc(maxV * sizeof(int));
    for (int i = 0; i < maxV; i++) first[i] = -1;
    for (int i = 0; i < elementsSize; i++) if (elements[i] < maxV && first[elements[i]] == -1) first[elements[i]] = i;
    int* ans = (int*)malloc(groupsSize * sizeof(int));
    for (int gi = 0; gi < groupsSize; gi++) {
        int g = groups[gi], best = -1;
        for (int d = 1; d * d <= g; d++) if (g % d == 0) {
            if (first[d] != -1 && (best == -1 || first[d] < best)) best = first[d];
            int other = g / d;
            if (first[other] != -1 && (best == -1 || first[other] < best)) best = first[other];
        }
        ans[gi] = best;
    }
    free(first);
    *returnSize = groupsSize;
    return ans;
}
