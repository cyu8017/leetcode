// LeetCode 0125 - Valid Palindrome
// https://leetcode.com/problems/valid-palindrome/

#include <string>
#include <cctype>
class Solution { public: bool isPalindrome(std::string s) {
    int left = 0, right = (int)s.size() - 1;
    while (left < right) {
        while (left < right && !std::isalnum((unsigned char)s[left])) ++left;
        while (left < right && !std::isalnum((unsigned char)s[right])) --right;
        if (std::tolower((unsigned char)s[left++]) != std::tolower((unsigned char)s[right--])) return false;
    }
    return true;
} };