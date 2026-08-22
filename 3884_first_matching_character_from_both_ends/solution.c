// LeetCode 3884 - First Matching Character From Both Ends
// https://leetcode.com/problems/first-matching-character-from-both-ends/

#include <string.h>

int firstMatchingIndex(char* s) {
    int n = (int)strlen(s);
    for (int i = 0; i < n / 2 + 1; i++) {
        if (s[i] == s[n - i - 1]) return i;
    }
    return -1;
}
