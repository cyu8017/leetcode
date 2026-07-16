// LeetCode 0242 - Valid Anagram
// https://leetcode.com/problems/valid-anagram/

#include <string>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        if (s.size() != t.size()) {
            return false;
        }
        int counts[26] = {0};
        for (int index = 0; index < static_cast<int>(s.size()); ++index) {
            counts[s[index] - 'a']++;
            counts[t[index] - 'a']--;
        }
        for (int count : counts) {
            if (count != 0) {
                return false;
            }
        }
        return true;
    }
};
