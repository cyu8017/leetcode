// LeetCode 2828 - Check if a String Is an Acronym of Words
// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

#include <stdbool.h>
#include <string.h>

bool isAcronym(char** words, int wordsSize, char* s) {
    if (wordsSize != (int)strlen(s)) return false;
    for (int i = 0; i < wordsSize; i++) {
        if (!words[i][0] || words[i][0] != s[i]) return false;
    }
    return true;
}
