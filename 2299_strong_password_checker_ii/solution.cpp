// LeetCode 2299 - Strong Password Checker II
// https://leetcode.com/problems/strong-password-checker-ii/

#include <string>

class Solution {
public:
    bool strongPasswordCheckerII(std::string password) {
        if (password.size() < 8) return false;
        const std::string special = "!@#$%^&*()-+";
        bool hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false;
        for (size_t i = 0; i < password.size(); ++i) {
            char c = password[i];
            if (i > 0 && c == password[i - 1]) return false;
            if (c >= 'a' && c <= 'z') hasLower = true;
            else if (c >= 'A' && c <= 'Z') hasUpper = true;
            else if (c >= '0' && c <= '9') hasDigit = true;
            else if (special.find(c) != std::string::npos) hasSpecial = true;
        }
        return hasLower && hasUpper && hasDigit && hasSpecial;
    }
};
