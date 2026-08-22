// LeetCode 1750 - Minimum Length of String After Deleting Similar Ends
// https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

#include <string.h>

int minimumLength(char* s) {
    int left = 0;
    int right = (int) strlen(s) - 1;
    while (left < right && s[left] == s[right]) {
        char ch = s[left];
        while (left <= right && s[left] == ch) {
            left++;
        }
        while (left <= right && s[right] == ch) {
            right--;
        }
    }
    return right - left + 1;
}
