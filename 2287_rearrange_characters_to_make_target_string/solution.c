// LeetCode 2287 - Rearrange Characters to Make Target String
// https://leetcode.com/problems/rearrange-characters-to-make-target-string/

#include <string.h>

int rearrangeCharacters(char* s, char* target) {
    int sc[26] = {0}, tc[26] = {0};
    for (int i = 0; s[i]; i++) sc[s[i] - 'a']++;
    for (int i = 0; target[i]; i++) tc[target[i] - 'a']++;
    int ans = 1000000000;
    for (int i = 0; i < 26; i++) {
        if (tc[i] == 0) continue;
        int v = sc[i] / tc[i];
        if (v < ans) ans = v;
    }
    return ans;
}
