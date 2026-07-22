// LeetCode 1658 - Minimum Operations to Reduce X to Zero
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int x) {
        long long total = std::accumulate(nums.begin(), nums.end(), 0LL);
        long long target = total - x;
        if (target < 0) {
            return -1;
        }
        int best = -1;
        int left = 0;
        long long cur = 0;
        for (int right = 0; right < static_cast<int>(nums.size()); ++right) {
            cur += nums[right];
            while (cur > target) {
                cur -= nums[left++];
            }
            if (cur == target) {
                best = std::max(best, right - left + 1);
            }
        }
        return best < 0 ? -1 : static_cast<int>(nums.size()) - best;
    }
};
