// LeetCode 3015 - Count the Number of Houses at a Certain Distance I
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

#include <stdlib.h>

static int iabs(int x) { return x < 0 ? -x : x; }
static int imin(int a, int b) { return a < b ? a : b; }

int* countOfPairs(int n, int x, int y, int* returnSize) {
    int* ans = (int*)calloc((size_t)n, sizeof(int));
    x--; y--;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int a = j - i;
            int b = iabs(x - i) + iabs(y - j) + 1;
            int c = iabs(x - j) + iabs(y - i) + 1;
            ans[imin(a, imin(b, c)) - 1] += 2;
        }
    }
    *returnSize = n;
    return ans;
}
