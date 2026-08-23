// LeetCode 3120 - Count the Number of Special Characters I
// https://leetcode.com/problems/count-the-number-of-special-characters-i/

#include <string>
#include <vector>

class Solution {
public:
    int numberOfSpecialChars(std::string word) {
        std::vector<bool> s(128);
        for (char c : word) s[(unsigned char)c] = true;
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (s['a' + i] && s['A' + i]) ans++;
        }
        return ans;
    }
};
