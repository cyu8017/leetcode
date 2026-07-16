// LeetCode 0409 - Longest Palindrome
// https://leetcode.com/problems/longest-palindrome/

#include <string.h>

int longestPalindrome(char* s) {
    int counts[256] = {0};
    for (int index = 0; s[index] != '\0'; index++) {
        counts[(unsigned char)s[index]] += 1;
    }

    int length = 0;
    int hasOdd = 0;
    for (int index = 0; index < 256; index++) {
        length += (counts[index] / 2) * 2;
        if (counts[index] % 2) {
            hasOdd = 1;
        }
    }

    return length + hasOdd;
}
