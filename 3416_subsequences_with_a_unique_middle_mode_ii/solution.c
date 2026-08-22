// LeetCode 3416 - Subsequences with a Unique Middle Mode II
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-ii/

#include <stdbool.h>

static bool uniqueMode3416(int* a, int n) {
    int best = 0, cnt = 0;
    for (int i = 0; i < n; i++) {
        int first = 1; for (int j = 0; j < i; j++) if (a[j] == a[i]) first = 0;
        if (!first) continue;
        int f = 0; for (int j = 0; j < n; j++) if (a[j] == a[i]) f++;
        if (f > best) { best = f; cnt = 1; } else if (f == best) cnt++;
    }
    return cnt == 1;
}

int subsequencesWithMiddleMode(int* nums, int numsSize) {
    const int mod = 1000000007;
    int n = numsSize, ans = 0;
    for (int mid = 2; mid < n - 2; mid++)
        for (int a = 0; a < mid; a++) for (int b = a + 1; b < mid; b++)
            for (int c = mid + 1; c < n; c++) for (int d = c + 1; d < n; d++) {
                int seq[5] = {nums[a], nums[b], nums[mid], nums[c], nums[d]};
                if (uniqueMode3416(seq, 5)) ans = (ans + 1) % mod;
            }
    return ans;
}
