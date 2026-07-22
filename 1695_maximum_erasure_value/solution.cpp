// LeetCode 1695 - Maximum Erasure Value
// https://leetcode.com/problems/maximum-erasure-value/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maximumUniqueSubarray(std::vector<int>& nums) {
        std::unordered_map<int, int> seen;
        int left = 0;
        int cur = 0;
        int best = 0;
        for (int right = 0; right < static_cast<int>(nums.size()); ++right) {
            int x = nums[right];
            if (seen.count(x) && seen[x] >= left) {
                int stop = seen[x];
                while (left <= stop) {
                    cur -= nums[left++];
                }
            }
            seen[x] = right;
            cur += x;
            best = std::max(best, cur);
        }
        return best;
    }
};
