// LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int maxCount(int* banned, int bannedSize, int n, int maxSum) {
    bool* ban = (bool*)calloc((size_t)(n + 1), sizeof(bool));
    for (int i = 0; i < bannedSize; i++) {
        if (banned[i] >= 1 && banned[i] <= n) ban[banned[i]] = true;
    }
    int ans = 0, sum = 0;
    for (int i = 1; i <= n; i++) {
        if (ban[i]) continue;
        if (sum + i > maxSum) break;
        sum += i;
        ans++;
    }
    free(ban);
    return ans;
}
