// LeetCode 0434 - Number of Segments in a String
// https://leetcode.com/problems/number-of-segments-in-a-string/

#include <stdbool.h>

int countSegments(char* s) {
    int count = 0;
    bool inSegment = false;
    for (int i = 0; s[i]; i++) {
        if (s[i] != ' ') {
            if (!inSegment) {
                count++;
                inSegment = true;
            }
        } else {
            inSegment = false;
        }
    }
    return count;
}
