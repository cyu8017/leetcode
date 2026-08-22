// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

#include <stdlib.h>

long long minCuttingCost(int n, int m, int k) {
    int x = n > m ? n : m;
    if (x <= k) return 0;
    return (long long)k * (x - k);
}
