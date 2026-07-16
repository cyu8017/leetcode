// LeetCode 0125 - Valid Palindrome
// https://leetcode.com/problems/valid-palindrome/

#include <ctype.h>
#include <string.h>
#include <stdbool.h>
bool isPalindrome(char* s) { int left=0,right=strlen(s)-1;while(left<right){while(left<right&&!isalnum((unsigned char)s[left]))left++;while(left<right&&!isalnum((unsigned char)s[right]))right--;if(tolower((unsigned char)s[left++])!=tolower((unsigned char)s[right--]))return false;}return true; }