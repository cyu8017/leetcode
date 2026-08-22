// LeetCode 2376 - Count Special Integers
// https://leetcode.com/problems/count-special-integers/

#include <stdbool.h>

int countSpecialNumbers(int n) {
    char s[12]; int m = 0;
    for (int x = n; x > 0; x /= 10) s[m++] = (char)('0' + x % 10);
    for (int i = 0; i < m / 2; i++) { char t = s[i]; s[i] = s[m - 1 - i]; s[m - 1 - i] = t; }
    int ans = 0, perm = 9;
    for (int i = 1; i < m; i++) { ans += perm; perm *= (10 - i); }
    bool used[10] = {0};
    for (int i = 0; i < m; i++) {
        int start = i == 0 ? 1 : 0;
        int digit = s[i] - '0';
        for (int d = start; d < digit; d++) {
            if (used[d]) continue;
            int rem = 10 - (i + 1), ways = 1;
            for (int j = i + 1; j < m; j++) { ways *= rem; rem--; }
            ans += ways;
        }
        if (used[digit]) return ans;
        used[digit] = true;
    }
    return ans + 1;
}
