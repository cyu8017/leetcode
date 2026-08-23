// LeetCode 0784 - Letter Case Permutation
// https://leetcode.com/problems/letter-case-permutation/

#include <cctype>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> letterCasePermutation(std::string s) {
        std::vector<std::string> result{""};
        for (char ch : s) {
            std::vector<std::string> next;
            if (std::isalpha(static_cast<unsigned char>(ch))) {
                char lower = static_cast<char>(std::tolower(static_cast<unsigned char>(ch)));
                char upper = static_cast<char>(std::toupper(static_cast<unsigned char>(ch)));
                for (const std::string& prefix : result) {
                    next.push_back(prefix + lower);
                    next.push_back(prefix + upper);
                }
            } else {
                for (const std::string& prefix : result) {
                    next.push_back(prefix + ch);
                }
            }
            result.swap(next);
        }
        return result;
    }
};
