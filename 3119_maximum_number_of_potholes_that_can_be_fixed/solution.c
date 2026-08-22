// LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
// https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/

#include <stdlib.h>
#include <string.h>

int maxPotholes(char* road, int budget) {
    int n = (int)strlen(road);
    int* cnt = calloc(n + 2, sizeof(int));
    int k = 0, ans = 0;
    for (int i = 0; i <= n; i++) {
        char c = (i < n) ? road[i] : '.';
        if (c == 'x') k++;
        else if (k > 0) { cnt[k]++; k = 0; }
    }
    for (k = n; k > 0 && budget > 0; k--) {
        int t = budget / (k + 1);
        if (t > cnt[k]) t = cnt[k];
        ans += t * k;
        budget -= t * (k + 1);
        cnt[k - 1] += cnt[k] - t;
    }
    free(cnt);
    return ans;
}
