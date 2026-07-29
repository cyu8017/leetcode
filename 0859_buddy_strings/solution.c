// LeetCode 0859 - Buddy Strings
// https://leetcode.com/problems/buddy-strings/

#include <stdbool.h>
#include <string.h>

bool buddyStrings(char* s, char* goal) {
    int n = (int)strlen(s);
    if (n != (int)strlen(goal)) return false;
    if (strcmp(s, goal) == 0) {
        int freq[26] = {0};
        for (int i = 0; i < n; i++) {
            if (++freq[s[i] - 'a'] > 1) return true;
        }
        return false;
    }
    int d1 = -1, d2 = -1;
    for (int i = 0; i < n; i++) {
        if (s[i] != goal[i]) {
            if (d1 < 0) d1 = i;
            else if (d2 < 0) d2 = i;
            else return false;
        }
    }
    return d2 >= 0 && s[d1] == goal[d2] && s[d2] == goal[d1];
}
