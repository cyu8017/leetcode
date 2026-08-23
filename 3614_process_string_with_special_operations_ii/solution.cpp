// LeetCode 3614 - Process String with Special Operations II
// https://leetcode.com/problems/process-string-with-special-operations-ii/

#include <string>

class Solution {
public:
    char processStr(std::string s, long long k) {
        long long m = 0;
        for (char c : s) {
            if (c == '*') m = m > 0 ? m - 1 : 0;
            else if (c == '#') m <<= 1;
            else if (c != '%') m += 1;
        }
        if (k >= m) return '.';
        for (int i = (int)s.size() - 1;; i--) {
            char c = s[i];
            if (c == '*') m += 1;
            else if (c == '#') {
                m /= 2;
                if (k >= m) k -= m;
            } else if (c == '%') {
                k = m - 1 - k;
            } else {
                m -= 1;
                if (k == m) return c;
            }
        }
    }
};
