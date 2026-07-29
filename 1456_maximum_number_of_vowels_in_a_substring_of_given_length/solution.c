// LeetCode 1456 - Maximum Number of Vowels in a Substring of Given Length
// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

#include <string.h>
#include <stdbool.h>

static bool is_vowel(char c) {
    return c=='a'||c=='e'||c=='i'||c=='o'||c=='u';
}

int maxVowels(char* s, int k) {
    int n = (int)strlen(s), cur = 0;
    for (int i = 0; i < k; i++) cur += is_vowel(s[i]);
    int ans = cur;
    for (int i = k; i < n; i++) {
        cur += is_vowel(s[i]) - is_vowel(s[i - k]);
        if (cur > ans) ans = cur;
    }
    return ans;
}
