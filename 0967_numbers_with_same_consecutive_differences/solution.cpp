// LeetCode 0967 - Numbers With Same Consecutive Differences
// https://leetcode.com/problems/numbers-with-same-consecutive-differences/

#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> numsSameConsecDiff(int n, int k) {
        std::vector<int> ans;
        auto dfs = [&](auto&& self, int num, int length) -> void {
            if (length == n) {
                ans.push_back(num);
                return;
            }
            int last = num % 10;
            std::unordered_set<int> nexts = {last + k, last - k};
            for (int nxt : nexts) {
                if (nxt >= 0 && nxt <= 9) self(self, num * 10 + nxt, length + 1);
            }
        };
        for (int start = 1; start <= 9; start++) dfs(dfs, start, 1);
        return ans;
    }
};
