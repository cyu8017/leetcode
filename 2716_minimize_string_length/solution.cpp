// LeetCode 2716 - Minimize String Length
// https://leetcode.com/problems/minimize-string-length/

#include <string>
#include <unordered_set>

class Solution {
public:
    int minimizedStringLength(std::string s) {
        return (int)std::unordered_set<char>(s.begin(), s.end()).size();
    }
};
