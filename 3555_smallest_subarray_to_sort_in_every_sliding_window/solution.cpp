// LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
// https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> minSubarraySort(std::vector<int>& nums, int k) {
        const int inf = 1 << 30;
        int n = (int)nums.size();
        auto f = [&](int i, int j) {
            int mi = inf, mx = -inf, l = -1, r = -1;
            for (int p = i; p <= j; p++) {
                if (nums[p] < mx) r = p;
                else mx = nums[p];
                int q = j - p + i;
                if (nums[q] > mi) l = q;
                else mi = nums[q];
            }
            if (r == -1) return 0;
            return r - l + 1;
        };
        std::vector<int> ans;
        for (int i = 0; i <= n - k; i++) ans.push_back(f(i, i + k - 1));
        return ans;
    }
};
