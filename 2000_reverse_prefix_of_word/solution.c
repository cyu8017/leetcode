// LeetCode 2000 - Reverse Prefix of Word
// https://leetcode.com/problems/reverse-prefix-of-word/

#include <string.h>
#include <stdlib.h>

char* reversePrefix(char* word, char ch) {
    char* pos = strchr(word, ch);
    if (!pos) {
        return word;
    }
    int left = 0;
    int right = (int)(pos - word);
    while (left < right) {
        char tmp = word[left];
        word[left] = word[right];
        word[right] = tmp;
        left++;
        right--;
    }
    return word;
}
