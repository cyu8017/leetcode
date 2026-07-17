// LeetCode 1784 - Check if Binary String Has at Most One Segment of Ones
// https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

#include <stdbool.h>
#include <string.h>

bool checkOnesSegment(char* s) {
    int start = 0;
    int end = strlen(s);
    while (start < end && s[start] == '0') start++;
    while (end > start && s[end - 1] == '0') end--;
    for (int i = start; i + 1 < end; i++) {
        if (s[i] == '0' && s[i + 1] == '1') {
            return false;
        }
    }
    return true;
}
