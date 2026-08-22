// LeetCode 2586 - Count the Number of Vowel Strings in Range
// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

#include <string.h>
#include <stdbool.h>

static bool isV(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int vowelStrings(char** words, int wordsSize, int left, int right) {
    (void)wordsSize;
    int ans = 0;
    for (int i = left; i <= right; i++) {
        int len = (int)strlen(words[i]);
        if (isV(words[i][0]) && isV(words[i][len - 1])) ans++;
    }
    return ans;
}
