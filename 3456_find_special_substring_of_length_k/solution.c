// LeetCode 3456 - Find Special Substring of Length K
// https://leetcode.com/problems/find-special-substring-of-length-k/

#include <stdbool.h>
#include <string.h>

bool hasSpecialSubstring(char* s, int k) {
    int n = (int)strlen(s);
    for (int i = 0; i + k <= n; i++) {
        int ok = 1;
        for (int j = i + 1; j < i + k; j++) {
            if (s[j] != s[i]) {
                ok = 0;
                break;
            }
        }
        if (!ok) continue;
        if (i > 0 && s[i - 1] == s[i]) continue;
        if (i + k < n && s[i + k] == s[i]) continue;
        return true;
    }
    return false;
}
