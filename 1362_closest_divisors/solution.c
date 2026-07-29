// LeetCode 1362 - Closest Divisors
// https://leetcode.com/problems/closest-divisors/

#include <stdlib.h>
#include <math.h>

int* closestDivisors(int num, int* returnSize) {
    int* best = (int*)malloc(2 * sizeof(int));
    best[0] = 1; best[1] = num + 1;
    int bestDiff = best[1] - best[0];
    for (int t = 0; t < 2; t++) {
        int x = num + 1 + t;
        int a = (int)sqrt((double)x);
        for (; a >= 1; a--) {
            if (x % a == 0) {
                int b = x / a;
                if (b - a < bestDiff) { best[0] = a; best[1] = b; bestDiff = b - a; }
                break;
            }
        }
    }
    *returnSize = 2;
    return best;
}
