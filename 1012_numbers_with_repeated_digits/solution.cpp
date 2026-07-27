// LeetCode 1012 - Numbers With Repeated Digits
// https://leetcode.com/problems/numbers-with-repeated-digits/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
    int p(int a, int b) {
        int res = 1;
        for (int i = 0; i < b; ++i) res *= a - i;
        return res;
    }

public:
    int numDupDigitsAtMostN(int n) {
        std::string s = std::to_string(n);
        int m = static_cast<int>(s.size());
        std::vector<int> digits(m);
        for (int i = 0; i < m; ++i) digits[i] = s[i] - '0';

        int totalUnique = 0;
        for (int length = 1; length < m; ++length) {
            totalUnique += 9 * p(9, length - 1);
        }

        std::unordered_set<int> used;
        bool broken = false;
        for (int i = 0; i < m; ++i) {
            int d = digits[i];
            for (int x = (i == 0 ? 1 : 0); x < d; ++x) {
                if (used.count(x)) continue;
                totalUnique += p(9 - i, m - i - 1);
            }
            if (used.count(d)) {
                broken = true;
                break;
            }
            used.insert(d);
        }
        if (!broken) ++totalUnique;
        return n - totalUnique;
    }
};

