// LeetCode 1546 - Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
// https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int maxNonOverlapping(std::vector<int>& nums, int target) {
        std::unordered_set<long long> seen{0};
        long long prefix = 0;
        int answer = 0;
        for (int value : nums) {
            prefix += value;
            if (seen.count(prefix - target)) {
                ++answer;
                prefix = 0;
                seen = {0};
            } else {
                seen.insert(prefix);
            }
        }
        return answer;
    }
};
