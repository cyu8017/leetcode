// LeetCode 1967 - Number of Strings That Appear as Substrings in Word
// https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

#include <string.h>

int numOfStrings(char** patterns, int patternsSize, char* word) {
    int ans = 0;
    for (int i = 0; i < patternsSize; i++) {
        if (strstr(word, patterns[i]) != NULL) ans++;
    }
    return ans;
}
