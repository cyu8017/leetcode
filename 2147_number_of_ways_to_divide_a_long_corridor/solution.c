// LeetCode 2147 - Number of Ways to Divide a Long Corridor
// https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

#include <stdlib.h>
#include <string.h>

int numberOfWays(char* corridor) {
    const int MOD = 1000000007;
    int n = (int)strlen(corridor);
    int* seats = (int*)malloc((size_t)n * sizeof(int));
    int sn = 0;
    for (int i = 0; i < n; i++) if (corridor[i] == 'S') seats[sn++] = i;
    if (sn == 0 || sn % 2 != 0) { free(seats); return 0; }
    long long ans = 1;
    for (int i = 2; i < sn; i += 2)
        ans = ans * (seats[i] - seats[i - 1]) % MOD;
    free(seats);
    return (int)ans;
}
