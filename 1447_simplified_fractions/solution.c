// LeetCode 1447 - Simplified Fractions
// https://leetcode.com/problems/simplified-fractions/

#include <stdlib.h>
#include <stdio.h>

static int gcd(int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; }

char** simplifiedFractions(int n, int* returnSize) {
    char** ans = (char**)malloc(n * n * sizeof(char*));
    int an = 0;
    for (int a = 1; a < n; a++)
        for (int b = a + 1; b <= n; b++)
            if (gcd(a, b) == 1) {
                ans[an] = (char*)malloc(16);
                sprintf(ans[an], "%d/%d", a, b);
                an++;
            }
    *returnSize = an;
    return ans;
}
