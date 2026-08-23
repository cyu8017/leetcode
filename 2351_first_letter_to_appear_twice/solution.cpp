// LeetCode 2351 - First Letter to Appear Twice
// https://leetcode.com/problems/first-letter-to-appear-twice/

#include <string>

class Solution {
public:
    char repeatedCharacter(std::string s) {
        bool seen[26] = {};
        for (char c : s) {
            int i = c - 'a';
            if (seen[i]) return c;
            seen[i] = true;
        }
        return 0;
    }
};
