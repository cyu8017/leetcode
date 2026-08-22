// LeetCode 2255 - Count Prefixes of a Given String
// https://leetcode.com/problems/count-prefixes-of-a-given-string/

#include <string.h>

int countPrefixes(char** words, int wordsSize, char* s) {
    int ans = 0;
    int slen = (int)strlen(s);
    for (int i = 0; i < wordsSize; i++) {
        int wlen = (int)strlen(words[i]);
        if (wlen <= slen && strncmp(s, words[i], (size_t)wlen) == 0) {
            ans++;
        }
    }
    return ans;
}
