// LeetCode 0520 - Detect Capital
// https://leetcode.com/problems/detect-capital/

#include <ctype.h>
#include <stdbool.h>
#include <string.h>

bool detectCapitalUse(char* word) {
    bool allUpper = true;
    bool allLower = true;
    const int length = (int)strlen(word);
    for (int index = 0; index < length; index++) {
        if (isupper((unsigned char)word[index])) {
            allLower = false;
        } else {
            allUpper = false;
        }
    }
    if (allUpper || allLower) {
        return true;
    }
    for (int index = 1; index < length; index++) {
        if (isupper((unsigned char)word[index])) {
            return false;
        }
    }
    return isupper((unsigned char)word[0]) != 0;
}
