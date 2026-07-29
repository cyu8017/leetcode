// LeetCode 0560 - Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int subarraySum(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> counts;
        counts[0] = 1;
        int prefix = 0;
        int answer = 0;
        for (int num : nums) {
            prefix += num;
            auto it = counts.find(prefix - k);
            if (it != counts.end()) {
                answer += it->second;
            }
            ++counts[prefix];
        }
        return answer;
    }
};
