// LeetCode 0058 - Length of Last Word
// https://leetcode.com/problems/length-of-last-word/

#include <string.h>

int lengthOfLastWord(char* s) {
    int length = 0;
    int i = (int)strlen(s) - 1;

    while (i >= 0 && s[i] == ' ') {
        i--;
    }

    while (i >= 0 && s[i] != ' ') {
        length++;
        i--;
    }

    return length;
}
