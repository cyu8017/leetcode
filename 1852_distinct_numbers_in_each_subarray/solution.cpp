// LeetCode 1852 - Distinct Numbers in Each Subarray
// https://leetcode.com/problems/distinct-numbers-in-each-subarray/

#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> distinctNumbers(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> counts;
        for (int i = 0; i < k; i++) {
            counts[nums[i]]++;
        }
        std::vector<int> result;
        result.push_back(static_cast<int>(counts.size()));
        int left = 0;
        for (int right = k; right < static_cast<int>(nums.size()); right++) {
            counts[nums[right]]++;
            int outgoing = nums[left];
            counts[outgoing]--;
            if (counts[outgoing] == 0) {
                counts.erase(outgoing);
            }
            left++;
            result.push_back(static_cast<int>(counts.size()));
        }
        return result;
    }
};
