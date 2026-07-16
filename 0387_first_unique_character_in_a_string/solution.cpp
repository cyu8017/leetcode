// LeetCode 0387 - First Unique Character in a String
// https://leetcode.com/problems/first-unique-character-in-a-string/

#include <string>

class Solution {
public:
    int firstUniqChar(std::string s) {
        int counts[26] = {};

        for (char ch : s) {
            counts[ch - 'a'] += 1;
        }

        for (int index = 0; index < static_cast<int>(s.size()); index++) {
            if (counts[s[index] - 'a'] == 1) {
                return index;
            }
        }

        return -1;
    }
};
