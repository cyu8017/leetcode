// LeetCode 2278 - Percentage of Letter in String
// https://leetcode.com/problems/percentage-of-letter-in-string/

#include <string.h>

int percentageLetter(char* s, char letter) {
    int cnt = 0;
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) {
        if (s[i] == letter) cnt++;
    }
    return cnt * 100 / n;
}
