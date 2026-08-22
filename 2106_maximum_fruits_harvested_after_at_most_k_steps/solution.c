// LeetCode 2106 - Maximum Fruits Harvested After at Most K Steps
// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

#include <stdlib.h>

static int minSteps2106(int left, int right, int start) {
    if (right <= start) return start - left;
    if (left >= start) return right - start;
    int a = (start - left) + (right - left);
    int b = (right - start) + (right - left);
    return a < b ? a : b;
}

int maxTotalFruits(int** fruits, int fruitsSize, int* fruitsColSize, int startPos, int k) {
    (void)fruitsColSize;
    int n = fruitsSize;
    int* pref = (int*)calloc((size_t)n + 1, sizeof(int));
    int* pos = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        pos[i] = fruits[i][0];
        pref[i + 1] = pref[i] + fruits[i][1];
    }
    int ans = 0, j = 0;
    for (int i = 0; i < n; i++) {
        while (j < n && minSteps2106(pos[i], pos[j], startPos) > k) j++;
        if (j <= i) {
            int sum = pref[i + 1] - pref[j];
            if (sum > ans) ans = sum;
        }
    }
    j = 0;
    for (int i = 0; i < n; i++) {
        while (j <= i && minSteps2106(pos[j], pos[i], startPos) > k) j++;
        int sum = pref[i + 1] - pref[j];
        if (sum > ans) ans = sum;
    }
    free(pref); free(pos);
    return ans;
}
