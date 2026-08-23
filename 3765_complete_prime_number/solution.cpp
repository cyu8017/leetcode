// LeetCode 3765 - Complete Prime Number
// https://leetcode.com/problems/complete-prime-number/

#include <string>

class Solution {
    bool isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; i++) if (x % i == 0) return false;
        return true;
    }

public:
    bool completePrime(int num) {
        std::string s = std::to_string(num);
        int x = 0;
        for (char c : s) {
            x = x * 10 + (c - '0');
            if (!isPrime(x)) return false;
        }
        x = 0;
        int p = 1;
        for (int i = (int)s.size() - 1; i >= 0; i--) {
            x = p * (s[i] - '0') + x;
            p *= 10;
            if (!isPrime(x)) return false;
        }
        return true;
    }
};
