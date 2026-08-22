// LeetCode 0065 - Valid Number
// https://leetcode.com/problems/valid-number/

#include <ctype.h>
#include <stdbool.h>
#include <string.h>

bool isNumber(char* s) {
    bool seenDigit = false;
    bool seenDot = false;
    bool seenExp = false;
    int length = (int)strlen(s);

    for (int i = 0; i < length; i++) {
        char ch = s[i];

        if (isdigit((unsigned char)ch)) {
            seenDigit = true;
        } else if (ch == '+' || ch == '-') {
            if (i > 0 && s[i - 1] != 'e' && s[i - 1] != 'E') {
                return false;
            }
        } else if (ch == 'e' || ch == 'E') {
            if (seenExp || !seenDigit) {
                return false;
            }
            seenExp = true;
            seenDigit = false;
            seenDot = false;
        } else if (ch == '.') {
            if (seenDot || seenExp) {
                return false;
            }
            seenDot = true;
        } else {
            return false;
        }
    }

    return seenDigit;
}
