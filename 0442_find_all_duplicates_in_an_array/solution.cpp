// LeetCode 0442 - Find All Duplicates in an Array
// https://leetcode.com/problems/find-all-duplicates-in-an-array/

#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<int> findDuplicates(std::vector<int>& nums) {
        std::vector<int> result;
        for (int number : nums) {
            int index = std::abs(number) - 1;
            if (nums[index] < 0) {
                result.push_back(std::abs(number));
            } else {
                nums[index] = -nums[index];
            }
        }
        return result;
    }
};
