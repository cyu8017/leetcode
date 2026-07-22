// LeetCode 1664 - Ways to Make a Fair Array
// https://leetcode.com/problems/ways-to-make-a-fair-array/

#include <vector>

class Solution {
public:
    int waysToMakeFair(std::vector<int>& nums) {
        int te = 0;
        int to = 0;
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            if (i % 2) {
                to += nums[i];
            } else {
                te += nums[i];
            }
        }
        int le = 0;
        int lo = 0;
        int ans = 0;
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            int x = nums[i];
            if (i % 2) {
                to -= x;
            } else {
                te -= x;
            }
            if (le + to == lo + te) {
                ++ans;
            }
            if (i % 2) {
                lo += x;
            } else {
                le += x;
            }
        }
        return ans;
    }
};
