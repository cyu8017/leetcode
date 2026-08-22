// LeetCode 3330 - Find the Original Typed String I
// https://leetcode.com/problems/find-the-original-typed-string-i/

#include <string.h>

int possibleStringCount(char* word) {
    int ans = 1;
    int n = (int)strlen(word);
    for (int i = 1; i < n; i++) if (word[i] == word[i - 1]) ans++;
    return ans;
}
