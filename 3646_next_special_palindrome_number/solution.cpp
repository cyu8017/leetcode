// LeetCode 3646 - Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    long long specialPalindrome(long long n) {
        std::vector<long long> cands;
        auto gen = [&](auto&& self, int mask) -> void {
            int total = 0, odd = 0;
            for (int d = 1; d <= 9; d++) {
                if ((mask >> d) & 1) {
                    total += d;
                    if (d % 2 == 1) odd++;
                }
            }
            if (total == 0 || total > 18 || odd > 1) return;
            int halfCnt[10] = {};
            int mid = 0;
            for (int d = 1; d <= 9; d++) {
                if (((mask >> d) & 1) == 0) continue;
                halfCnt[d] = d / 2;
                if (d % 2 == 1) mid = d;
            }
            int halfLen = total / 2;
            auto dfs = [&](auto&& dfs_self, int pos, std::vector<int>& cur) -> void {
                if (pos == halfLen) {
                    std::string left, s;
                    for (int x : cur) left += char('0' + x);
                    s = left;
                    if (mid > 0) s += char('0' + mid);
                    for (int i = (int)left.size() - 1; i >= 0; i--) s += left[i];
                    cands.push_back(std::stoll(s));
                    return;
                }
                for (int d = 1; d <= 9; d++) {
                    if (halfCnt[d] == 0) continue;
                    halfCnt[d]--;
                    cur.push_back(d);
                    dfs_self(dfs_self, pos + 1, cur);
                    cur.pop_back();
                    halfCnt[d]++;
                }
            };
            std::vector<int> cur;
            dfs(dfs, 0, cur);
        };
        for (int mask = 1; mask < (1 << 10); mask++) {
            if (mask & 1) continue;
            gen(gen, mask);
        }
        std::sort(cands.begin(), cands.end());
        for (long long v : cands)
            if (v > n) return v;
        return -1;
    }
};
