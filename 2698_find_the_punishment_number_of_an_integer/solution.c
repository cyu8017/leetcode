// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

static bool canPartition2698(const char* s, int target) {
    if (target < 0) return false;
    if (*s == '\0') return target == 0;
    int val = 0;
    for (int i = 0; s[i]; i++) {
        val = val * 10 + (s[i] - '0');
        if (canPartition2698(s + i + 1, target - val)) return true;
    }
    return false;
}

int punishmentNumber(int n) {
    int ans = 0;
    char buf[32];
    for (int i = 1; i <= n; i++) {
        int sq = i * i;
        sprintf(buf, "%d", sq);
        if (canPartition2698(buf, i)) ans += sq;
    }
    return ans;
}
