// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

#include <string>

class Solution {
public:
    bool isSumEqual(std::string firstWord, std::string secondWord, std::string targetWord) {
        return value(firstWord) + value(secondWord) == value(targetWord);
    }

private:
    long long value(const std::string& word) {
        long long result = 0;
        for (char ch : word) {
            result = result * 10 + (ch - 'a');
        }
        return result;
    }
};
