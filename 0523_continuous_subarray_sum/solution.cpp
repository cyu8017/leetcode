// LeetCode 0523 - Continuous Subarray Sum
// https://leetcode.com/problems/continuous-subarray-sum/

#include <unordered_map>
#include <vector>

class Solution {
public:
    bool checkSubarraySum(std::vector<int>& nums, int k) {
        long long prefix = 0;
        std::unordered_map<long long, int> remainders;
        remainders[0] = -1;

        for (int index = 0; index < static_cast<int>(nums.size()); ++index) {
            prefix += nums[index];
            const long long mod = k != 0 ? prefix % k : prefix;
            const auto found = remainders.find(mod);
            if (found != remainders.end()) {
                if (index - found->second >= 2) {
                    return true;
                }
            } else {
                remainders[mod] = index;
            }
        }
        return false;
    }
};
