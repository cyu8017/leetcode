// LeetCode 0848 - Shifting Letters
// https://leetcode.com/problems/shifting-letters/

#include <string>
#include <vector>

class Solution {
public:
    std::string shiftingLetters(std::string s, std::vector<int>& shifts) {
        int total = 0;
        for (int i = static_cast<int>(s.size()) - 1; i >= 0; --i) {
            total = (total + shifts[i]) % 26;
            s[i] = static_cast<char>((s[i] - 'a' + total) % 26 + 'a');
        }
        return s;
    }
};
