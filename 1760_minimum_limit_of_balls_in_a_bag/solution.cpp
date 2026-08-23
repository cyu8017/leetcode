// LeetCode 1760 - Minimum Limit of Balls in a Bag
// https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minimumSize(std::vector<int>& nums, int maxOperations) {
        int lo = 1;
        int hi = *std::max_element(nums.begin(), nums.end());
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            long long ops = 0;
            for (int x : nums) {
                ops += (x - 1) / mid;
            }
            if (ops <= maxOperations) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
};
