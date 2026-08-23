// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        std::unordered_set<int> need;
        for (int i = 1; i <= k; i++) need.insert(i);
        for (int i = (int)nums.size() - 1; i >= 0; i--) {
            need.erase(nums[i]);
            if (need.empty()) return (int)nums.size() - i;
        }
        return (int)nums.size();
    }
};
