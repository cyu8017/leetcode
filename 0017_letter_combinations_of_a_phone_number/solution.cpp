// LeetCode 0017 - Letter Combinations of a Phone Number
// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

#include <string>
#include <vector>

class Solution {
    static const std::vector<std::string> MAPPING;

    void backtrack(
        const std::string& digits,
        int index,
        std::string& path,
        std::vector<std::string>& result
    ) {
        if (index == static_cast<int>(digits.size())) {
            result.push_back(path);
            return;
        }
        for (char ch : MAPPING[digits[index] - '0']) {
            path.push_back(ch);
            backtrack(digits, index + 1, path, result);
            path.pop_back();
        }
    }

public:
    std::vector<std::string> letterCombinations(std::string digits) {
        std::vector<std::string> result;
        if (digits.empty()) {
            return result;
        }
        std::string path;
        backtrack(digits, 0, path, result);
        return result;
    }
};

const std::vector<std::string> Solution::MAPPING = {
    "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
};
