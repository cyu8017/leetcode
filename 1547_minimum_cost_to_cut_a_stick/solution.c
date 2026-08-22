// LeetCode 1547 - Minimum Cost to Cut a Stick
// https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int minCost(int n, int* cuts, int cutsSize) {
    int size = cutsSize + 2;
    int* points = (int*)malloc((size_t)size * sizeof(int));
    points[0] = 0;
    for (int i = 0; i < cutsSize; i++) points[i + 1] = cuts[i];
    points[size - 1] = n;
    qsort(points + 1, (size_t)cutsSize, sizeof(int), cmpInt);

    int** dp = (int**)malloc((size_t)size * sizeof(int*));
    for (int i = 0; i < size; i++) dp[i] = (int*)calloc((size_t)size, sizeof(int));

    for (int width = 2; width < size; width++) {
        for (int left = 0; left + width < size; left++) {
            int right = left + width;
            int best = 1000000000;
            for (int mid = left + 1; mid < right; mid++) {
                int cand = dp[left][mid] + dp[mid][right];
                if (cand < best) best = cand;
            }
            if (right > left + 1) best += points[right] - points[left];
            else best = 0;
            dp[left][right] = best;
        }
    }
    int ans = dp[0][size - 1];
    for (int i = 0; i < size; i++) free(dp[i]);
    free(dp);
    free(points);
    return ans;
}
