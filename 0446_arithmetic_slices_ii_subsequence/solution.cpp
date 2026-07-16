// LeetCode 0446 - Arithmetic Slices II - Subsequence
// https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int numberOfArithmeticSlices(std::vector<int>& nums) {
        int total = 0;
        std::vector<std::unordered_map<long long, int>> differences(nums.size());

        for (size_t index = 0; index < nums.size(); ++index) {
            for (size_t previous = 0; previous < index; ++previous) {
                long long diff = static_cast<long long>(nums[index]) - nums[previous];
                total += differences[previous][diff];
                differences[index][diff] += differences[previous][diff] + 1;
            }
        }
        return total;
    }
};
