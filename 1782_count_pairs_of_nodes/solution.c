// LeetCode 1782 - Count Pairs Of Nodes
// https://leetcode.com/problems/count-pairs-of-nodes/

#include <stdlib.h>
#include <string.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int cmpLongLong(const void* a, const void* b) {
    long long x = *(const long long*)a;
    long long y = *(const long long*)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countPairs(int n, int** edges, int edgesSize, int* edgesColSize, int* queries, int queriesSize, int* returnSize) {
    int* deg = (int*)calloc(n + 1, sizeof(int));
    long long* keys = (long long*)malloc(edgesSize * sizeof(long long));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0];
        int b = edges[i][1];
        if (a > b) {
            int tmp = a;
            a = b;
            b = tmp;
        }
        deg[a]++;
        deg[b]++;
        keys[i] = (long long)a * 100000 + b;
    }
    qsort(keys, edgesSize, sizeof(long long), cmpLongLong);
    int* sortedDeg = (int*)malloc(n * sizeof(int));
    memcpy(sortedDeg, deg + 1, n * sizeof(int));
    qsort(sortedDeg, n, sizeof(int), cmpInt);
    int* ans = (int*)malloc(queriesSize * sizeof(int));
    for (int qi = 0; qi < queriesSize; qi++) {
        int q = queries[qi];
        int res = 0;
        int left = 0;
        int right = n - 1;
        while (left < right) {
            if (sortedDeg[left] + sortedDeg[right] > q) {
                res += right - left;
                right--;
            } else {
                left++;
            }
        }
        int i = 0;
        while (i < edgesSize) {
            int j = i;
            while (j < edgesSize && keys[j] == keys[i]) {
                j++;
            }
            int count = j - i;
            int a = (int)(keys[i] / 100000);
            int b = (int)(keys[i] % 100000);
            int sum = deg[a] + deg[b];
            if (sum > q && q >= sum - count) {
                res--;
            }
            i = j;
        }
        ans[qi] = res;
    }
    free(deg);
    free(keys);
    free(sortedDeg);
    *returnSize = queriesSize;
    return ans;
}
