// LeetCode 2063 - Vowels of All Substrings
// https://leetcode.com/problems/vowels-of-all-substrings/

#include <string.h>
#include <stdbool.h>

static bool isVowel2063(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

long long countVowels(char* word) {
    int n = (int)strlen(word);
    long long ans = 0;
    for (int i = 0; i < n; i++) if (isVowel2063(word[i])) ans += (long long)(i + 1) * (n - i);
    return ans;
}
