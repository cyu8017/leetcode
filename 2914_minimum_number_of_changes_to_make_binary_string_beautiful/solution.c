// LeetCode 2914 - Minimum Number of Changes to Make Binary String Beautiful
// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

#include <string.h>

int minChanges(char* s) {
    int ans = 0, n = (int)strlen(s);
    for (int i = 0; i < n; i += 2) if (s[i] != s[i + 1]) ans++;
    return ans;
}
