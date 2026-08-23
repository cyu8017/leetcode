// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

#include <cstdint>
#include <string>
#include <vector>

class Solution {
    bool dfs(std::vector<char>& res, int i, bool tight, bool sameLen, const std::string& num, long long t) {
        if (i == (int)res.size()) {
            long long prod = 1;
            for (char c : res) {
                prod *= (c - '0');
                if (prod == 0) break;
            }
            return prod % t == 0 && prod > 0;
        }
        char start = (i == 0) ? '1' : '0';
        if (tight && sameLen && i < (int)num.size()) start = num[i];
        for (char c = start; c <= '9'; c++) {
            res[i] = c;
            bool nt = tight && sameLen && i < (int)num.size() && c == num[i];
            if (dfs(res, i + 1, nt, sameLen, num, t)) return true;
        }
        return false;
    }

public:
    std::string smallestNumber(std::string num, long long t) {
        long long tt = t;
        for (int d = 9; d >= 2; d--) {
            while (tt % d == 0) tt /= d;
        }
        if (tt > 1) return "-1";
        for (int extra = 0; extra <= 60; extra++) {
            int L = (int)num.size() + extra;
            std::vector<char> res(L);
            if (dfs(res, 0, true, extra == 0, num, t)) return std::string(res.begin(), res.end());
        }
        return "-1";
    }
};
