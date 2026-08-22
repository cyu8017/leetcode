// LeetCode 2185 - Counting Words With a Given Prefix
// https://leetcode.com/problems/counting-words-with-a-given-prefix/

#include <string.h>

int prefixCount(char** words, int wordsSize, char* pref) {
    int ans = 0, plen = (int)strlen(pref);
    for (int i = 0; i < wordsSize; i++)
        if (strncmp(words[i], pref, (size_t)plen) == 0) ans++;
    return ans;
}
