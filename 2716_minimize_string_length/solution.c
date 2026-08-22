// LeetCode 2716 - Minimize String Length
// https://leetcode.com/problems/minimize-string-length/

#include <stdbool.h>

int minimizedStringLength(char* s) {
    bool seen[26] = {0};
    for (int i = 0; s[i]; i++) seen[s[i] - 'a'] = true;
    int ans = 0;
    for (int i = 0; i < 26; i++) if (seen[i]) ans++;
    return ans;
}
