// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

#include <string.h>

long long minimumCost(char* s) {
    long long ans = 0;
    int n = (int)strlen(s);
    for (int i = 1; i < n; i++) {
        if (s[i] != s[i - 1]) {
            int left = i, right = n - i;
            ans += left < right ? left : right;
        }
    }
    return ans;
}
