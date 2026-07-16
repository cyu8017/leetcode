// LeetCode 0266 - Palindrome Permutation
// https://leetcode.com/problems/palindrome-permutation/

#include <stdbool.h>

bool canPermutePalindrome(char* s) {
    int counts[26] = {0};
    for (int index = 0; s[index] != '\0'; ++index) {
        counts[s[index] - 'a']++;
    }
    int odd = 0;
    for (int index = 0; index < 26; ++index) {
        if (counts[index] % 2 != 0) {
            odd++;
        }
    }
    return odd <= 1;
}
