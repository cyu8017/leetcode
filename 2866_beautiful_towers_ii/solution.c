// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

#include <stdlib.h>

long long maximumSumOfHeights(int* maxHeights, int maxHeightsSize) {
    int n = maxHeightsSize;
    long long* left = (long long*)calloc(n, sizeof(long long));
    int* st = (int*)malloc((n + 2) * sizeof(int));
    int top = 0;
    st[top++] = -1;
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        while (top > 1 && maxHeights[st[top - 1]] >= maxHeights[i]) {
            int j = st[--top];
            sum -= (long long)maxHeights[j] * (j - st[top - 1]);
        }
        sum += (long long)maxHeights[i] * (i - st[top - 1]);
        left[i] = sum;
        st[top++] = i;
    }
    long long* right = (long long*)calloc(n, sizeof(long long));
    top = 0;
    st[top++] = n;
    sum = 0;
    for (int i = n - 1; i >= 0; i--) {
        while (top > 1 && maxHeights[st[top - 1]] >= maxHeights[i]) {
            int j = st[--top];
            sum -= (long long)maxHeights[j] * (st[top - 1] - j);
        }
        sum += (long long)maxHeights[i] * (st[top - 1] - i);
        right[i] = sum;
        st[top++] = i;
    }
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        long long cand = left[i] + right[i] - maxHeights[i];
        if (cand > ans) ans = cand;
    }
    free(left); free(right); free(st);
    return ans;
}
