// LeetCode 0360 - Sort Transformed Array
// https://leetcode.com/problems/sort-transformed-array/

#include <vector>

class Solution {
public:
    std::vector<int> sortTransformedArray(std::vector<int>& nums, int a, int b, int c) {
        auto transform = [a, b, c](int value) {
            return a * value * value + b * value + c;
        };

        int left = 0;
        int right = static_cast<int>(nums.size()) - 1;
        std::vector<int> result(nums.size());
        int index = a > 0 ? static_cast<int>(nums.size()) - 1 : 0;
        int step = a > 0 ? -1 : 1;

        while (left <= right) {
            int leftValue = transform(nums[left]);
            int rightValue = transform(nums[right]);

            if (a > 0) {
                if (leftValue > rightValue) {
                    result[index] = leftValue;
                    left += 1;
                } else {
                    result[index] = rightValue;
                    right -= 1;
                }
            } else if (leftValue < rightValue) {
                result[index] = leftValue;
                left += 1;
            } else {
                result[index] = rightValue;
                right -= 1;
            }

            index += step;
        }

        return result;
    }
};
