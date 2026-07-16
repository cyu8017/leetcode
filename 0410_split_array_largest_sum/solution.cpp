// LeetCode 0410 - Split Array Largest Sum
// https://leetcode.com/problems/split-array-largest-sum/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        int left = *max_element(nums.begin(), nums.end());
        int right = accumulate(nums.begin(), nums.end(), 0);

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (canSplit(nums, k, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

private:
    bool canSplit(const vector<int>& nums, int k, int limit) {
        int parts = 1;
        int current = 0;

        for (int value : nums) {
            if (current + value > limit) {
                ++parts;
                current = 0;
            }
            current += value;
        }

        return parts <= k;
    }
};
