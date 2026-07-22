// LeetCode 1616 - Split Two Strings to Make Palindrome
// https://leetcode.com/problems/split-two-strings-to-make-palindrome/

#include <string>

class Solution {
    static bool isPal(const std::string& s, int i, int j) {
        while (i < j) {
            if (s[i] != s[j]) {
                return false;
            }
            ++i;
            --j;
        }
        return true;
    }

    static bool check(const std::string& x, const std::string& y) {
        int i = 0, j = static_cast<int>(x.size()) - 1;
        while (i < j && x[i] == y[j]) {
            ++i;
            --j;
        }
        return isPal(x, i, j) || isPal(y, i, j);
    }

public:
    bool checkPalindromeFormation(std::string a, std::string b) {
        return check(a, b) || check(b, a);
    }
};
