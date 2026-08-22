// LeetCode 3395 - Subsequences with a Unique Middle Mode I
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/

#include <stdbool.h>

static bool uniqueMode(int* a, int n) {
    int best = 0, cnt = 0;
    for (int i = 0; i < n; i++) {
        int f = 0;
        for (int j = 0; j < n; j++) if (a[j] == a[i]) f++;
        int first = 1;
        for (int j = 0; j < i; j++) if (a[j] == a[i]) first = 0;
        if (!first) continue;
        if (f > best) { best = f; cnt = 1; }
        else if (f == best) cnt++;
    }
    return cnt == 1;
}

int subsequencesWithMiddleMode(int* nums, int numsSize) {
    const int mod = 1000000007;
    int n = numsSize, ans = 0;
    for (int mid = 2; mid < n - 2; mid++)
        for (int a = 0; a < mid; a++)
            for (int b = a + 1; b < mid; b++)
                for (int c = mid + 1; c < n; c++)
                    for (int d = c + 1; d < n; d++) {
                        int seq[5] = {nums[a], nums[b], nums[mid], nums[c], nums[d]};
                        if (uniqueMode(seq, 5)) ans++;
                    }
    return ans % mod;
}
