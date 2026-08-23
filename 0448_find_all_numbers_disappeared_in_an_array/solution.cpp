// LeetCode 0448 - Find All Numbers Disappeared in an Array
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<int> findDisappearedNumbers(std::vector<int>& nums) {
        for (int number : nums) {
            int index = std::abs(number) - 1;
            if (nums[index] > 0) {
                nums[index] = -nums[index];
            }
        }

        std::vector<int> result;
        for (size_t index = 0; index < nums.size(); ++index) {
            if (nums[index] > 0) {
                result.push_back(static_cast<int>(index + 1));
            }
        }
        return result;
    }
};
