// LeetCode 1295 - Find Numbers with Even Number of Digits
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

#include <string>
#include <vector>

class Solution {
public:
    int findNumbers(std::vector<int>& nums) {
        int answer = 0;
        for (int value : nums) {
            if (std::to_string(value).size() % 2 == 0) {
                ++answer;
            }
        }
        return answer;
    }
};
