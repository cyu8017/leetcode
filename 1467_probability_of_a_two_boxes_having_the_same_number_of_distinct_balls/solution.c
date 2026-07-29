// LeetCode 1467 - Probability of a Two Boxes Having the Same Number of Distinct Balls
// https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/

#include <stdlib.h>

static long long comb[50][50];
static long long good_c, total_c;
static int* balls_g;
static int ballsSize_g;
static int half_g;

static void dfs(int i, int left, int dl, long long ways) {
    if (i == ballsSize_g) {
        if (left == half_g) {
            total_c += ways;
            if (dl == 0) good_c += ways;
        }
        return;
    }
    for (int x = 0; x <= balls_g[i]; x++) {
        if (left + x <= half_g)
            dfs(i + 1, left + x, dl + (x > 0) - (x < balls_g[i]), ways * comb[balls_g[i]][x]);
    }
}

double getProbability(int* balls, int ballsSize) {
    for (int i = 0; i < 50; i++) {
        comb[i][0] = comb[i][i] = 1;
        for (int j = 1; j < i; j++) comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
    }
    int sum = 0;
    for (int i = 0; i < ballsSize; i++) sum += balls[i];
    half_g = sum / 2;
    balls_g = balls; ballsSize_g = ballsSize;
    good_c = total_c = 0;
    dfs(0, 0, 0, 1);
    return (double)good_c / (double)total_c;
}
