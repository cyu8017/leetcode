// LeetCode 0219 - Contains Duplicate II
// https://leetcode.com/problems/contains-duplicate-ii/

#include <unordered_map>
#include <vector>

class Solution {
public:
    bool containsNearbyDuplicate(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> lastIndex;
        for (int i = 0; i < static_cast<int>(nums.size()); i++) {
            auto it = lastIndex.find(nums[i]);
            if (it != lastIndex.end() && i - it->second <= k) {
                return true;
            }
            lastIndex[nums[i]] = i;
        }
        return false;
    }
};
