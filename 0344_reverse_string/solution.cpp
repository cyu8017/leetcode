// LeetCode 0344 - Reverse String
// https://leetcode.com/problems/reverse-string/

#include <vector>

class Solution {
public:
    void reverseString(std::vector<char>& s) {
        int left = 0;
        int right = static_cast<int>(s.size()) - 1;
        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left += 1;
            right -= 1;
        }
    }
};
