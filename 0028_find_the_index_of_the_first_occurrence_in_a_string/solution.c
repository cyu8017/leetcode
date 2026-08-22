// LeetCode 0028 - Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

#include <string.h>

int strStr(char* haystack, char* needle) {
    if (needle == NULL || needle[0] == '\0') {
        return 0;
    }

    int haystackLen = (int)strlen(haystack);
    int needleLen = (int)strlen(needle);

    for (int i = 0; i <= haystackLen - needleLen; i++) {
        if (strncmp(haystack + i, needle, (size_t)needleLen) == 0) {
            return i;
        }
    }

    return -1;
}
