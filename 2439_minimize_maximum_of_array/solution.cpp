// LeetCode 2439 - Minimize Maximum of Array
// https://leetcode.com/problems/minimize-maximum-of-array/

#include <vector>

class Solution {
public:
    int minimizeArrayValue(std::vector<int>& nums) {
        long long sum = 0;
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            sum += nums[i];
            int avg = (int)((sum + i) / (i + 1));
            if (avg > ans) ans = avg;
        }
        return ans;
    }
};
