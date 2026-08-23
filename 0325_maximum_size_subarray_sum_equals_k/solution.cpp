// LeetCode 0325 - Maximum Size Subarray Sum Equals k
// https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maxSubArrayLen(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> prefixIndex;
        prefixIndex[0] = -1;
        int prefix = 0;
        int best = 0;
        for (int index = 0; index < static_cast<int>(nums.size()); index++) {
            prefix += nums[index];
            auto found = prefixIndex.find(prefix - k);
            if (found != prefixIndex.end()) {
                best = std::max(best, index - found->second);
            }
            if (prefixIndex.find(prefix) == prefixIndex.end()) {
                prefixIndex[prefix] = index;
            }
        }
        return best;
    }
};
