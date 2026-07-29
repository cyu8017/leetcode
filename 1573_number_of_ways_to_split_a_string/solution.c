// LeetCode 1573 - Number of Ways to Split a String
// https://leetcode.com/problems/number-of-ways-to-split-a-string/

#include <stdlib.h>
#include <string.h>

int numWays(char* s) {
    const int MOD = 1000000007;
    int n = (int)strlen(s);
    int ones = 0;
    for (int i = 0; i < n; i++) if (s[i] == '1') ones++;
    if (ones % 3) return 0;
    if (ones == 0) {
        long long gaps = n - 1;
        return (int)(gaps * (gaps - 1) / 2 % MOD);
    }
    int target = ones / 3;
    int* positions = (int*)malloc((size_t)ones * sizeof(int));
    int p = 0;
    for (int i = 0; i < n; i++) if (s[i] == '1') positions[p++] = i;
    long long a = positions[target] - positions[target - 1];
    long long b = positions[2 * target] - positions[2 * target - 1];
    free(positions);
    return (int)(a * b % MOD);
}
