// LeetCode 3978 - Unique Middle Element
// https://leetcode.com/problems/unique-middle-element/

#include <vector>

class Solution {
public:
    bool isMiddleElementUnique(std::vector<int>& nums) {
        int mid = nums[nums.size() / 2];
        int cnt = 0;
        for (int x : nums) {
            if (x == mid) cnt++;
        }
        return cnt == 1;
    }
};
