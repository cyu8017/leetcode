// LeetCode 1961 - Check If String Is a Prefix of Array
// https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

#include <stdbool.h>
#include <string.h>

bool isPrefixString(char* s, char** words, int wordsSize) {
    int pos = 0;
    int n = (int)strlen(s);
    for (int i = 0; i < wordsSize; i++) {
        int len = (int)strlen(words[i]);
        if (pos + len > n) return false;
        if (strncmp(s + pos, words[i], (size_t)len) != 0) return false;
        pos += len;
        if (pos == n) return true;
    }
    return pos == n;
}
