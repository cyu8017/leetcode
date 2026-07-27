// LeetCode 1060 - Missing Element in Sorted Array
// https://leetcode.com/problems/missing-element-in-sorted-array/

#include <vector>

class Solution {
public:
    int missingElement(std::vector<int>& nums, int k) {
        auto missing = [&](int i) { return nums[i] - nums[0] - i; };
        int n = static_cast<int>(nums.size());
        if (k > missing(n - 1)) {
            return nums.back() + k - missing(n - 1);
        }
        int lo = 0;
        int hi = n - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (missing(mid) < k) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return nums[lo - 1] + k - missing(lo - 1);
    }
};
