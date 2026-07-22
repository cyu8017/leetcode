// LeetCode 1668 - Maximum Repeating Substring
// https://leetcode.com/problems/maximum-repeating-substring/

#include <string>

class Solution {
public:
    int maxRepeating(std::string sequence, std::string word) {
        int k = 0;
        std::string cur = word;
        while (sequence.find(cur) != std::string::npos) {
            ++k;
            cur += word;
        }
        return k;
    }
};
