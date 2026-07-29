// LeetCode 0902 - Numbers At Most N Given Digit Set
// https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

#include <string>
#include <vector>

class Solution {
public:
    int atMostNGivenDigitSet(std::vector<std::string>& digits, int n) {
        std::string s = std::to_string(n);
        int m = (int)s.size();
        int k = (int)digits.size();

        auto ipow = [](int base, int exp) {
            int r = 1;
            while (exp-- > 0) r *= base;
            return r;
        };

        auto countUpTo = [&](auto&& self, const std::string& t) -> int {
            if (t.empty()) return 0;
            int first = 0;
            for (const auto& d : digits) {
                if (d[0] < t[0]) first++;
            }
            int ways = first * ipow(k, (int)t.size() - 1);
            bool found = false;
            for (const auto& d : digits) {
                if (d[0] == t[0]) {
                    found = true;
                    break;
                }
            }
            if (found) ways += self(self, t.substr(1));
            return ways;
        };

        int ans = 0;
        for (int i = 1; i < m; i++) ans += ipow(k, i);
        ans += countUpTo(countUpTo, s);
        return ans;
    }
};
