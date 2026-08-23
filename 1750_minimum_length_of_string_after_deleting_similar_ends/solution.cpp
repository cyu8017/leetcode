// LeetCode 1750 - Minimum Length of String After Deleting Similar Ends
// https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

#include <string>

class Solution {
public:
    int minimumLength(std::string s) {
        int left = 0;
        int right = static_cast<int>(s.size()) - 1;
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
};
