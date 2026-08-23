// LeetCode 3606 - Coupon Code Validator
// https://leetcode.com/problems/coupon-code-validator/

#include <algorithm>
#include <cctype>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<std::string> validateCoupons(std::vector<std::string>& code,
                                             std::vector<std::string>& businessLine,
                                             std::vector<bool>& isActive) {
        std::unordered_set<std::string> bs = {"electronics", "grocery", "pharmacy", "restaurant"};
        auto check = [](const std::string& s) {
            if (s.empty()) return false;
            for (char c : s)
                if (!std::isalnum((unsigned char)c) && c != '_') return false;
            return true;
        };
        std::vector<int> idx;
        for (int i = 0; i < (int)code.size(); i++) {
            if (isActive[i] && bs.count(businessLine[i]) && check(code[i])) idx.push_back(i);
        }
        std::sort(idx.begin(), idx.end(), [&](int i, int j) {
            if (businessLine[i] != businessLine[j]) return businessLine[i] < businessLine[j];
            return code[i] < code[j];
        });
        std::vector<std::string> ans;
        for (int i : idx) ans.push_back(code[i]);
        return ans;
    }
};
