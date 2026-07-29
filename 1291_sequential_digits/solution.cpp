// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> sequentialDigits(int low, int high) {
        const std::string digits = "123456789";
        std::vector<int> answer;
        for (int length = 2; length <= 9; ++length) {
            for (int start = 0; start + length <= 9; ++start) {
                int value = std::stoi(digits.substr(start, length));
                if (value >= low && value <= high) {
                    answer.push_back(value);
                }
            }
        }
        return answer;
    }
};
