// LeetCode 3941 - Password Strength
// https://leetcode.com/problems/password-strength/

#include <cctype>
#include <string>
#include <unordered_set>

class Solution {
public:
    int passwordStrength(std::string password) {
        std::unordered_set<char> st(password.begin(), password.end());
        int ans = 0;
        for (char ch : st) {
            if (std::islower((unsigned char)ch)) ans += 1;
            else if (std::isupper((unsigned char)ch)) ans += 2;
            else if (std::isdigit((unsigned char)ch)) ans += 3;
            else ans += 5;
        }
        return ans;
    }
};
