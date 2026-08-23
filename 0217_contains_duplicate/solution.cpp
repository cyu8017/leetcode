// LeetCode 0217 - Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/

#include <unordered_set>
#include <vector>

class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> seen;
        for (int num : nums) {
            if (!seen.insert(num).second) {
                return true;
            }
        }
        return false;
    }
};
