// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

#include <algorithm>
#include <vector>

class Solution {
public:
    int smallestDivisor(std::vector<int>& nums, int threshold) {
        int lo = 1, hi = *std::max_element(nums.begin(), nums.end());
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            long long total = 0;
            for (int x : nums) {
                total += (x + mid - 1) / mid;
            }
            if (total <= threshold) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
};
