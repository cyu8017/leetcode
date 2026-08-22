// LeetCode 2611 - Mice and Cheese
// https://leetcode.com/problems/mice-and-cheese/

#include <stdlib.h>

static int cmpDesc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

int miceAndCheese(int* reward1, int reward1Size, int* reward2, int reward2Size, int k) {
    (void)reward2Size;
    int n = reward1Size;
    int* diff = (int*)malloc((size_t)n * sizeof(int));
    int ans = 0;
    for (int i = 0; i < n; i++) {
        ans += reward2[i];
        diff[i] = reward1[i] - reward2[i];
    }
    qsort(diff, (size_t)n, sizeof(int), cmpDesc);
    for (int i = 0; i < k; i++) ans += diff[i];
    free(diff);
    return ans;
}
