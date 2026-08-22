// LeetCode 3136 - Valid Word
// https://leetcode.com/problems/valid-word/

#include <stdbool.h>
#include <ctype.h>
#include <string.h>

bool isValid(char* word) {
    int n = (int)strlen(word);
    if (n < 3) return false;
    bool hasVowel = false, hasConsonant = false;
    bool vs[26] = {0};
    const char* vowels = "aeiou";
    for (int i = 0; vowels[i]; i++) vs[vowels[i] - 'a'] = true;
    for (int i = 0; i < n; i++) {
        unsigned char c = word[i];
        if (isalpha(c)) {
            if (vs[tolower(c) - 'a']) hasVowel = true;
            else hasConsonant = true;
        } else if (!isdigit(c)) return false;
    }
    return hasVowel && hasConsonant;
}
