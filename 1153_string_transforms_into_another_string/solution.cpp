// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

#include <string>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    bool canConvert(std::string str1, std::string str2) {
        if (str1 == str2) return true;
        std::unordered_map<char, char> mapping;
        for (size_t i = 0; i < str1.size(); ++i) {
            if (mapping.count(str1[i]) && mapping[str1[i]] != str2[i]) return false;
            mapping[str1[i]] = str2[i];
        }
        return std::unordered_set<char>(str2.begin(), str2.end()).size() < 26;
    }
};
