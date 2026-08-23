// LeetCode 3768 - Minimum Inversion Count in Subarrays of Fixed Length
// https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minInversionCount(std::vector<int>& nums, int k) {
        std::vector<int> vals = nums;
        std::sort(vals.begin(), vals.end());
        vals.erase(std::unique(vals.begin(), vals.end()), vals.end());
        std::vector<int> bit(vals.size() + 1, 0);
        auto add = [&](int i, int delta) {
            for (; i < (int)bit.size(); i += i & -i) bit[i] += delta;
        };
        auto sum = [&](int i) {
            int res = 0;
            for (; i > 0; i -= i & -i) res += bit[i];
            return res;
        };
        std::vector<int> rank(nums.size());
        long long inv = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            rank[i] = (int)(std::lower_bound(vals.begin(), vals.end(), nums[i]) - vals.begin()) + 1;
            if (i < k) {
                inv += i - sum(rank[i]);
                add(rank[i], 1);
            }
        }
        long long best = inv;
        for (int r = k; r < (int)nums.size(); r++) {
            int left = rank[r - k];
            inv -= sum(left - 1);
            add(left, -1);
            inv += k - 1 - sum(rank[r]);
            add(rank[r], 1);
            if (inv < best) best = inv;
        }
        return best;
    }
};
