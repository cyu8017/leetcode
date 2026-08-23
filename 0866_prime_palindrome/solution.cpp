// LeetCode 0866 - Prime Palindrome
// https://leetcode.com/problems/prime-palindrome/

#include <cmath>
#include <string>

class Solution {
public:
    int primePalindrome(int n) {
        auto isPrime = [](int x) {
            if (x < 2) {
                return false;
            }
            if (x % 2 == 0) {
                return x == 2;
            }
            for (int d = 3; d * 1LL * d <= x; d += 2) {
                if (x % d == 0) {
                    return false;
                }
            }
            return true;
        };

        if (n <= 2) {
            return 2;
        }
        if (n <= 3) {
            return 3;
        }
        if (n <= 5) {
            return 5;
        }
        if (n <= 7) {
            return 7;
        }
        if (n <= 11) {
            return 11;
        }

        for (int length = 1; length <= 5; ++length) {
            int start = static_cast<int>(std::pow(10, length - 1));
            int end = static_cast<int>(std::pow(10, length));
            for (int root = start; root < end; ++root) {
                std::string s = std::to_string(root);
                std::string pal = s;
                for (int i = static_cast<int>(s.size()) - 2; i >= 0; --i) {
                    pal.push_back(s[i]);
                }
                int val = std::stoi(pal);
                if (val >= n && isPrime(val)) {
                    return val;
                }
            }
        }
        return 0;
    }
};
