// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

#include <string>
#include <vector>
#include <map>
#include <array>
#include <algorithm>

class Solution {
    static const int MOD = 1000000007;
    // convert decimal string to base-b digits (MSB first) using repeated division
    std::vector<int> toDigits(std::string s, int b) {
        if (s == "0") return {0};
        std::vector<int> digs;
        while (!(s.size() == 1 && s[0] == '0')) {
            int rem = 0;
            std::string q;
            for (char c : s) {
                int cur = rem * 10 + (c - '0');
                int d = cur / b;
                rem = cur % b;
                if (!q.empty() || d != 0) q.push_back(char('0' + d));
            }
            digs.push_back(rem);
            s = q.empty() ? "0" : q;
        }
        std::reverse(digs.begin(), digs.end());
        return digs;
    }
    std::string dec(std::string s) {
        int i = (int)s.size() - 1;
        while (i >= 0 && s[i] == '0') { s[i] = '9'; i--; }
        if (i < 0) return "0";
        s[i]--;
        if (s[0] == '0' && s.size() > 1) s.erase(s.begin());
        // trim leading zeros
        size_t p = 0;
        while (p + 1 < s.size() && s[p] == '0') p++;
        return s.substr(p);
    }
    int countUpto(const std::vector<int>& digs, int b) {
        int m = (int)digs.size();
        std::map<std::array<int, 3>, int> memo;
        auto dfs = [&](auto&& self, int pos, int last, bool tight) -> int {
            if (pos == m) return 1;
            std::array<int, 3> key = {pos, last, tight ? 1 : 0};
            if (memo.count(key)) return memo[key];
            int up = tight ? digs[pos] : b - 1;
            int res = 0;
            for (int d = last; d <= up; d++)
                res = (res + self(self, pos + 1, d, tight && d == up)) % MOD;
            return memo[key] = res;
        };
        return dfs(dfs, 0, 0, true);
    }
public:
    int countNumbers(std::string l, std::string r, int b) {
        auto rd = toDigits(r, b);
        auto ld = toDigits(dec(l), b);
        return (countUpto(rd, b) - countUpto(ld, b) + MOD) % MOD;
    }
};
