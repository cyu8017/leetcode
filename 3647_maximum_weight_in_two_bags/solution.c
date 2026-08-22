// LeetCode 3647 - Maximum Weight in Two Bags
// https://leetcode.com/problems/maximum-weight-in-two-bags/

#include <stdlib.h>
static int imax(int a,int b){return a>b?a:b;}
int maxWeight(int* weights, int weightsSize, int w1, int w2) {
    int** f = (int**)malloc((size_t)(w1 + 1) * sizeof(int*));
    for (int i = 0; i <= w1; i++) f[i] = (int*)calloc((size_t)(w2 + 1), sizeof(int));
    for (int t = 0; t < weightsSize; t++) {
        int x = weights[t];
        for (int j = w1; j >= 0; j--) {
            for (int k = w2; k >= 0; k--) {
                if (x <= j) f[j][k] = imax(f[j][k], f[j - x][k] + x);
                if (x <= k) f[j][k] = imax(f[j][k], f[j][k - x] + x);
            }
        }
    }
    int ans = f[w1][w2];
    for (int i = 0; i <= w1; i++) free(f[i]);
    free(f);
    return ans;
}
