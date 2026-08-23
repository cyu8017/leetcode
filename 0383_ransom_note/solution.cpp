// LeetCode 0383 - Ransom Note
// https://leetcode.com/problems/ransom-note/

#include <string>

class Solution {
public:
    bool canConstruct(std::string ransomNote, std::string magazine) {
        int counts[26] = {};

        for (char ch : magazine) {
            counts[ch - 'a'] += 1;
        }

        for (char ch : ransomNote) {
            if (counts[ch - 'a'] == 0) {
                return false;
            }
            counts[ch - 'a'] -= 1;
        }

        return true;
    }
};
