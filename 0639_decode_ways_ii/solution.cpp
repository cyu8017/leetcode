// LeetCode 0639 - Decode Ways II
// https://leetcode.com/problems/decode-ways-ii/

#include <string>

class Solution {
    static int one(char ch) {
        if (ch == '*') {
            return 9;
        }
        if (ch == '0') {
            return 0;
        }
        return 1;
    }

    static int two(char a, char b) {
        if (a == '*' && b == '*') {
            return 15;
        }
        if (a == '*') {
            return b <= '6' ? 2 : 1;
        }
        if (b == '*') {
            if (a == '1') {
                return 9;
            }
            if (a == '2') {
                return 6;
            }
            return 0;
        }
        const int value = (a - '0') * 10 + (b - '0');
        return value >= 10 && value <= 26 ? 1 : 0;
    }

public:
    int numDecodings(std::string s) {
        constexpr int mod = 1000000007;
        long long prev2 = 1;
        long long prev1 = one(s[0]);
        for (std::size_t i = 1; i < s.size(); ++i) {
            const long long cur =
                (one(s[i]) * prev1 + two(s[i - 1], s[i]) * prev2) % mod;
            prev2 = prev1;
            prev1 = cur;
        }
        return static_cast<int>(prev1);
    }
};
