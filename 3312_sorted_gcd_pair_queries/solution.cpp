// LeetCode 3312 - Sorted GCD Pair Queries
// https://leetcode.com/problems/sorted-gcd-pair-queries/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    std::vector<int> gcdValues(std::vector<int>& nums, std::vector<long long>& queries) {
        int maxV = *std::max_element(nums.begin(), nums.end());
        std::vector<int> cnt(maxV + 1);
        for (int x : nums) cnt[x]++;
        std::vector<int64_t> divCnt(maxV + 1);
        for (int g = 1; g <= maxV; g++) {
            int64_t c = 0;
            for (int m = g; m <= maxV; m += g) c += cnt[m];
            divCnt[g] = c * (c - 1) / 2;
        }
        std::vector<int64_t> exact(maxV + 1);
        for (int g = maxV; g >= 1; g--) {
            exact[g] = divCnt[g];
            for (int m = 2 * g; m <= maxV; m += g) exact[g] -= exact[m];
        }
        std::vector<int64_t> pref(maxV + 1);
        for (int g = 1; g <= maxV; g++) pref[g] = pref[g - 1] + exact[g];
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            long long q = queries[i];
            int lo = 1, hi = maxV;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (pref[mid] > q) hi = mid;
                else lo = mid + 1;
            }
            ans[i] = lo;
        }
        return ans;
    }
};
