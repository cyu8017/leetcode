// LeetCode 0345 - Reverse Vowels of a String
// https://leetcode.com/problems/reverse-vowels-of-a-string/

#include <string.h>

static int isVowel(char ch) {
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'
        || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U';
}

char* reverseVowels(char* s) {
    int left = 0;
    int right = (int)strlen(s) - 1;

    while (left < right) {
        while (left < right && !isVowel(s[left])) {
            left += 1;
        }
        while (left < right && !isVowel(s[right])) {
            right -= 1;
        }
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left += 1;
        right -= 1;
    }

    return s;
}
