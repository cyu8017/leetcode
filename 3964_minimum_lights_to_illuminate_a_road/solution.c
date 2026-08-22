// LeetCode 3964 - Minimum Lights To Illuminate A Road
// https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/

#include <stdlib.h>

int minLights(int* lights, int lightsSize) {
    int n = lightsSize;
    int* d = calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) {
        int v = lights[i];
        if (v > 0) {
            int l = i - v; if (l < 0) l = 0;
            int r = i + v; if (r > n - 1) r = n - 1;
            d[l]++;
            if (r + 1 < n) d[r + 1]--;
        }
    }
    int s = 0, cnt = 0, ans = 0;
    for (int i = 0; i < n; i++) {
        s += d[i];
        if (s == 0) cnt++;
        else { ans += (cnt + 2) / 3; cnt = 0; }
    }
    ans += (cnt + 2) / 3;
    free(d);
    return ans;
}
