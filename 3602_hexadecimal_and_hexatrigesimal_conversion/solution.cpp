// LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
// https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

#include <algorithm>
#include <string>

class Solution {
    std::string f(int x, int k) {
        std::string res;
        while (x > 0) {
            int v = x % k;
            res.push_back(v <= 9 ? char('0' + v) : char('A' + v - 10));
            x /= k;
        }
        std::reverse(res.begin(), res.end());
        return res;
    }

public:
    std::string concatHex36(int n) {
        return f(n * n, 16) + f(n * n * n, 36);
    }
};
