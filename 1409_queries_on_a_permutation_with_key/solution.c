// LeetCode 1409 - Queries on a Permutation With Key
// https://leetcode.com/problems/queries-on-a-permutation-with-key/

#include <stdlib.h>

int* processQueries(int* queries, int queriesSize, int m, int* returnSize) {
    int* values = (int*)malloc(m * sizeof(int));
    for (int i = 0; i < m; i++) values[i] = i + 1;
    int* ans = (int*)malloc(queriesSize * sizeof(int));
    for (int q = 0; q < queriesSize; q++) {
        int index = 0;
        while (values[index] != queries[q]) index++;
        ans[q] = index;
        int v = values[index];
        for (int i = index; i > 0; i--) values[i] = values[i - 1];
        values[0] = v;
    }
    free(values);
    *returnSize = queriesSize;
    return ans;
}
