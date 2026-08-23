// LeetCode 0018 - 4Sum
// https://leetcode.com/problems/4sum/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> fourSum(std::vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> result;

        for (int i = 0; i < static_cast<int>(nums.size()) - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            for (int j = i + 1; j < static_cast<int>(nums.size()) - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }

                int left = j + 1;
                int right = static_cast<int>(nums.size()) - 1;
                while (left < right) {
                    long long total =
                        static_cast<long long>(nums[i]) + nums[j] + nums[left] + nums[right];
                    if (total == target) {
                        result.push_back({nums[i], nums[j], nums[left], nums[right]});
                        while (left < right && nums[left] == nums[left + 1]) {
                            left++;
                        }
                        while (left < right && nums[right] == nums[right - 1]) {
                            right--;
                        }
                        left++;
                        right--;
                    } else if (total < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        return result;
    }
};
