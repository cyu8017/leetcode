// LeetCode 2451 - Odd String Difference
// https://leetcode.com/problems/odd-string-difference/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool sameDiff(char* a, char* b) {
    int n = (int)strlen(a);
    for (int i = 1; i < n; i++) {
        if ((a[i] - a[i - 1]) != (b[i] - b[i - 1])) return false;
    }
    return true;
}

char* oddString(char** words, int wordsSize) {
    if (sameDiff(words[0], words[1])) {
        for (int i = 2; i < wordsSize; i++) {
            if (!sameDiff(words[i], words[0])) return words[i];
        }
    }
    if (sameDiff(words[2], words[0])) return words[1];
    return words[0];
}
