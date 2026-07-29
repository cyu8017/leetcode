// LeetCode 0791 - Custom Sort String
// https://leetcode.com/problems/custom-sort-string/

#include <string>

class Solution {
public:
    std::string customSortString(std::string order, std::string s) {
        int counts[26] = {};
        for (char ch : s) {
            ++counts[ch - 'a'];
        }
        std::string parts;
        for (char ch : order) {
            while (counts[ch - 'a'] > 0) {
                parts.push_back(ch);
                --counts[ch - 'a'];
            }
        }
        for (int i = 0; i < 26; ++i) {
            while (counts[i] > 0) {
                parts.push_back(static_cast<char>('a' + i));
                --counts[i];
            }
        }
        return parts;
    }
};
