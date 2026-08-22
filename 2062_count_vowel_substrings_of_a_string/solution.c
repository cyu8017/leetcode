// LeetCode 2062 - Count Vowel Substrings of a String
// https://leetcode.com/problems/count-vowel-substrings-of-a-string/

#include <string.h>
#include <stdbool.h>

static bool isVowel2062(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int countVowelSubstrings(char* word) {
    int ans = 0, n = (int)strlen(word);
    for (int i = 0; i < n; i++) {
        int seen = 0;
        for (int j = i; j < n && isVowel2062(word[j]); j++) {
            if (word[j] == 'a') seen |= 1;
            else if (word[j] == 'e') seen |= 2;
            else if (word[j] == 'i') seen |= 4;
            else if (word[j] == 'o') seen |= 8;
            else seen |= 16;
            if (seen == 31) ans++;
        }
    }
    return ans;
}
