// LeetCode 0970 - Powerful Integers
// https://leetcode.com/problems/powerful-integers/

#include <stdlib.h>

int* powerfulIntegers(int x, int y, int bound, int* returnSize) {
    int* ans = (int*)malloc(400 * sizeof(int));
    int n = 0;
    long long a = 1;
    while (a < bound) {
        long long b = 1;
        while (a + b <= bound) {
            int v = (int)(a + b);
            int found = 0;
            for (int i = 0; i < n; i++) if (ans[i] == v) { found = 1; break; }
            if (!found) ans[n++] = v;
            if (y == 1) break;
            b *= y;
        }
        if (x == 1) break;
        a *= x;
    }
    *returnSize = n;
    return ans;
}
