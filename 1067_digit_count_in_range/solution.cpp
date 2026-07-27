// LeetCode 1067 - Digit Count in Range
// https://leetcode.com/problems/digit-count-in-range/

#include <string>

class Solution {
public:
    int digitsCount(int d, int low, int high) {
        auto ipow10 = [](int exp) {
            int p = 1;
            while (exp-- > 0) {
                p *= 10;
            }
            return p;
        };
        auto countUpto = [&](int n) -> int {
            if (n < 0) {
                return 0;
            }
            std::string s = std::to_string(n);
            int length = static_cast<int>(s.size());
            int ans = 0;
            for (int i = 0; i < length; ++i) {
                int left = i ? std::stoi(s.substr(0, i)) : 0;
                int right = (i + 1 < length) ? std::stoi(s.substr(i + 1)) : 0;
                int digit = s[i] - '0';
                int power = ipow10(length - i - 1);
                if (d != 0) {
                    ans += left * power;
                    if (digit > d) {
                        ans += power;
                    } else if (digit == d) {
                        ans += right + 1;
                    }
                } else {
                    if (i == 0) {
                        continue;
                    }
                    ans += (left - 1) * power;
                    if (digit > 0) {
                        ans += power;
                    } else {
                        ans += right + 1;
                    }
                }
            }
            return ans;
        };
        return countUpto(high) - countUpto(low - 1);
    }
};
