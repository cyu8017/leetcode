// LeetCode 1816 - Truncate Sentence
// https://leetcode.com/problems/truncate-sentence/

#include <sstream>
#include <string>

class Solution {
public:
    std::string truncateSentence(std::string s, int k) {
        std::istringstream iss(s);
        std::string word;
        std::string result;
        int count = 0;
        while (iss >> word && count < k) {
            if (!result.empty()) {
                result.push_back(' ');
            }
            result += word;
            ++count;
        }
        return result;
    }
};
