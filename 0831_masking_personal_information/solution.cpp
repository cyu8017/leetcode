// LeetCode 0831 - Masking Personal Information
// https://leetcode.com/problems/masking-personal-information/

#include <cctype>
#include <string>

class Solution {
public:
    std::string maskPII(std::string s) {
        auto at = s.find('@');
        if (at != std::string::npos) {
            for (char& ch : s) {
                ch = static_cast<char>(std::tolower(static_cast<unsigned char>(ch)));
            }
            at = s.find('@');
            std::string name = s.substr(0, at);
            std::string domain = s.substr(at + 1);
            return std::string(1, name.front()) + "*****" + name.back() + "@" + domain;
        }
        std::string digits;
        for (char ch : s) {
            if (std::isdigit(static_cast<unsigned char>(ch))) {
                digits.push_back(ch);
            }
        }
        std::string local = digits.substr(digits.size() - 4);
        int country = static_cast<int>(digits.size()) - 10;
        if (country == 0) {
            return "***-***-" + local;
        }
        return "+" + std::string(country, '*') + "-***-***-" + local;
    }
};
