// LeetCode 1662 - Check If Two String Arrays are Equivalent
// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

#include <string>
#include <vector>

class Solution {
public:
    bool arrayStringsAreEqual(std::vector<std::string>& word1, std::vector<std::string>& word2) {
        std::string a;
        std::string b;
        for (const auto& w : word1) {
            a += w;
        }
        for (const auto& w : word2) {
            b += w;
        }
        return a == b;
    }
};
