// LeetCode 3110 - Score of a String
// https://leetcode.com/problems/score-of-a-string/

#include <string.h>
#include <stdlib.h>

int scoreOfString(char* s) {
    int ans = 0, n = (int)strlen(s);
    for (int i = 1; i < n; i++) ans += abs((int)s[i - 1] - (int)s[i]);
    return ans;
}
