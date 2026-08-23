// LeetCode 3533 - Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/

#include <vector>
#include <algorithm>
#include <map>

class Solution {
public:
    std::vector<int> concatenatedDivisibility(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        std::vector<int> pows(n);
        for (int i = 0; i < n; i++) {
            int p = 1, num = nums[i];
            if (num == 0) p = 10 % k;
            else {
                for (int x = num; x > 0; x /= 10) p = p * 10 % k;
            }
            pows[i] = p;
        }
        std::map<std::pair<int, int>, bool> memo;
        auto dp = [&](auto&& self, int mask, int mod) -> bool {
            if (mask == (1 << n) - 1) return mod == 0;
            auto kk = std::make_pair(mask, mod);
            if (memo.count(kk)) return memo[kk];
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 0) {
                    int nm = (mod * pows[i] + nums[i]) % k;
                    if (self(self, mask | (1 << i), nm)) return memo[kk] = true;
                }
            }
            return memo[kk] = false;
        };
        auto reconstruct = [&](auto&& self, int mask, int mod) -> std::vector<int> {
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 0) {
                    int nm = (mod * pows[i] + nums[i]) % k;
                    if (dp(dp, mask | (1 << i), nm)) {
                        auto rest = self(self, mask | (1 << i), nm);
                        rest.insert(rest.begin(), nums[i]);
                        return rest;
                    }
                }
            }
            return {};
        };
        if (!dp(dp, 0, 0)) return {};
        return reconstruct(reconstruct, 0, 0);
    }
};
