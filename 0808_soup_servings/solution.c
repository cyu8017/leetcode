// LeetCode 0808 - Soup Servings
// https://leetcode.com/problems/soup-servings/

#include <stdlib.h>

static double* memo;
static int dim;

static double dp(int a, int b) {
    if (a <= 0 && b <= 0) return 0.5;
    if (a <= 0) return 1.0;
    if (b <= 0) return 0.0;
    double* cell = &memo[a * dim + b];
    if (*cell >= 0) return *cell;
    *cell = 0.25 * (dp(a - 4, b) + dp(a - 3, b - 1) + dp(a - 2, b - 2) + dp(a - 1, b - 3));
    return *cell;
}

double soupServings(int n) {
    if (n >= 4800) return 1.0;
    int units = (n + 24) / 25;
    dim = units + 1;
    memo = (double*)malloc((size_t)dim * (size_t)dim * sizeof(double));
    for (int i = 0; i < dim * dim; i++) memo[i] = -1.0;
    double ans = dp(units, units);
    free(memo);
    return ans;
}
