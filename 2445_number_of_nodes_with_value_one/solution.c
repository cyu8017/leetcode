// LeetCode 2445 - Number of Nodes With Value One
// https://leetcode.com/problems/number-of-nodes-with-value-one/

#include <stdlib.h>
#include <string.h>

int numberOfNodes(int n, int* queries, int queriesSize) {
    int* flip = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < queriesSize; i++) flip[queries[i]] ^= 1;
    int ans = 0;
    int* val = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 1; i <= n; i++) {
        val[i] = flip[i];
        if (i > 1) val[i] ^= val[i / 2];
        ans += val[i];
    }
    free(flip);
    free(val);
    return ans;
}
