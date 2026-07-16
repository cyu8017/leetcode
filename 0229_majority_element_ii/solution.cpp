// LeetCode 0229 - Majority Element II
// https://leetcode.com/problems/majority-element-ii/

#include <optional>
#include <vector>

class Solution {
public:
    std::vector<int> majorityElement(std::vector<int>& nums) {
        std::optional<int> candidate1;
        std::optional<int> candidate2;
        int count1 = 0;
        int count2 = 0;

        for (int num : nums) {
            if (candidate1.has_value() && num == candidate1.value()) {
                count1++;
            } else if (candidate2.has_value() && num == candidate2.value()) {
                count2++;
            } else if (count1 == 0) {
                candidate1 = num;
                count1 = 1;
            } else if (count2 == 0) {
                candidate2 = num;
                count2 = 1;
            } else {
                count1--;
                count2--;
            }
        }

        count1 = 0;
        count2 = 0;
        for (int num : nums) {
            if (candidate1.has_value() && num == candidate1.value()) {
                count1++;
            } else if (candidate2.has_value() && num == candidate2.value()) {
                count2++;
            }
        }

        int threshold = static_cast<int>(nums.size()) / 3;
        std::vector<int> result;
        if (count1 > threshold) {
            result.push_back(candidate1.value());
        }
        if (candidate2.has_value() && candidate2 != candidate1 && count2 > threshold) {
            result.push_back(candidate2.value());
        }
        return result;
    }
};
