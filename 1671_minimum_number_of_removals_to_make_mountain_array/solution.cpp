// LeetCode 1671 - Minimum Number of Removals to Make Mountain Array
// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

#include <algorithm>
#include <vector>

class Solution {
    std::vector<int> lis(const std::vector<int>& a) {
        std::vector<int> d;
        std::vector<int> out;
        for (int x : a) {
            auto it = std::lower_bound(d.begin(), d.end(), x);
            int i = static_cast<int>(it - d.begin());
            if (it == d.end()) {
                d.push_back(x);
            } else {
                *it = x;
            }
            out.push_back(i + 1);
        }
        return out;
    }

public:
    int minimumMountainRemovals(std::vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        std::vector<int> left = lis(nums);
        std::vector<int> rev = nums;
        std::reverse(rev.begin(), rev.end());
        std::vector<int> right = lis(rev);
        std::reverse(right.begin(), right.end());
        int best = 0;
        for (int i = 0; i < n; ++i) {
            if (left[i] > 1 && right[i] > 1) {
                best = std::max(best, left[i] + right[i] - 1);
            }
        }
        return n - best;
    }
};
