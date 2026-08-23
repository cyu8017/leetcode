// LeetCode 3309 - Maximum Possible Number by Binary Concatenation
// https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

#include <string>
#include <vector>

class Solution {
    std::string toBin(int x) {
        if (x == 0) return "0";
        std::string s;
        while (x > 0) {
            s.insert(s.begin(), char('0' + (x & 1)));
            x >>= 1;
        }
        return s;
    }

public:
    int maxGoodNumber(std::vector<int>& nums) {
        std::string bs[3];
        for (int i = 0; i < 3; i++) bs[i] = toBin(nums[i]);
        int idx[3] = {0, 1, 2};
        int ans = 0;
        auto perm = [&](auto&& self, int i) -> void {
            if (i == 3) {
                std::string s = bs[idx[0]] + bs[idx[1]] + bs[idx[2]];
                int v = 0;
                for (char c : s) v = v * 2 + (c - '0');
                if (v > ans) ans = v;
                return;
            }
            for (int j = i; j < 3; j++) {
                std::swap(idx[i], idx[j]);
                self(self, i + 1);
                std::swap(idx[i], idx[j]);
            }
        };
        perm(perm, 0);
        return ans;
    }
};
