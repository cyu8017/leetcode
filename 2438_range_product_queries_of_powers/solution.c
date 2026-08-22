// LeetCode 2438 - Range Product Queries of Powers
// https://leetcode.com/problems/range-product-queries-of-powers/

#include <stdlib.h>

int* productQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    const int mod = 1000000007;
    int powers[32], pc = 0;
    for (int bit = 0; bit < 31; bit++) if ((n >> bit) & 1) powers[pc++] = 1 << bit;
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        long long prod = 1;
        for (int j = queries[i][0]; j <= queries[i][1]; j++)
            prod = prod * powers[j] % mod;
        ans[i] = (int)prod;
    }
    *returnSize = queriesSize;
    return ans;
}
