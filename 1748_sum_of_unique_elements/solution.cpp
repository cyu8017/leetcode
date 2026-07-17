// LeetCode 1748 - Sum of Unique Elements
// https://leetcode.com/problems/sum-of-unique-elements/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int sumOfUnique(std::vector<int>& nums) {
        std::unordered_map<int, int> counts;
        for (int value : nums) {
            counts[value]++;
        }
        int total = 0;
        for (const auto& [value, count] : counts) {
            if (count == 1) {
                total += value;
            }
        }
        return total;
    }
};
