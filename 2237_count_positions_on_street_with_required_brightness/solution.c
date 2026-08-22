// LeetCode 2237 - Count Positions on Street With Required Brightness
// https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

#include <stdlib.h>

int meetRequirement(int n, int** lights, int lightsSize, int* lightsColSize, int* requirement, int requirementSize) {
    (void)lightsColSize; (void)requirementSize;
    int* diff = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < lightsSize; i++) {
        int pos = lights[i][0], r = lights[i][1];
        int l = pos - r;
        if (l < 0) l = 0;
        int rr = pos + r;
        if (rr >= n) rr = n - 1;
        diff[l]++;
        diff[rr + 1]--;
    }
    int ans = 0, cur = 0;
    for (int i = 0; i < n; i++) {
        cur += diff[i];
        if (cur >= requirement[i]) ans++;
    }
    free(diff);
    return ans;
}
