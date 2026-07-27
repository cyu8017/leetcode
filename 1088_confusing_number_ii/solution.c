// LeetCode 1088 - Confusing Number II
// https://leetcode.com/problems/confusing-number-ii/

#include <stdbool.h>

static int rotateMap[10] = {0, 1, -1, -1, -1, -1, 9, -1, 8, 6};
static int digits[5] = {0, 1, 6, 8, 9};

static bool isConfusing(long long num) {
    long long original = num;
    long long rotated = 0;
    while (num) {
        int d = (int)(num % 10);
        rotated = rotated * 10 + rotateMap[d];
        num /= 10;
    }
    return rotated != original;
}

static void dfs(long long cur, long long n, int* ans) {
    if (cur > n) {
        return;
    }
    if (cur && isConfusing(cur)) {
        (*ans)++;
    }
    if (cur == 0) {
        int start[4] = {1, 6, 8, 9};
        for (int i = 0; i < 4; i++) {
            dfs(start[i], n, ans);
        }
    } else {
        for (int i = 0; i < 5; i++) {
            dfs(cur * 10 + digits[i], n, ans);
        }
    }
}

int confusingNumberII(int n) {
    int ans = 0;
    dfs(0, n, &ans);
    return ans;
}
