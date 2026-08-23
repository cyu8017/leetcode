// LeetCode 2366 - Minimum Replacements to Sort the Array
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

#include <vector>

class Solution {
public:
    long long minimumReplacement(std::vector<int>& nums) {
        long long ans = 0;
        int n = (int)nums.size();
        int prev = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] <= prev) {
                prev = nums[i];
                continue;
            }
            int parts = (nums[i] + prev - 1) / prev;
            ans += parts - 1;
            prev = nums[i] / parts;
        }
        return ans;
    }
};
