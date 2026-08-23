// LeetCode 2860 - Happy Students
// https://leetcode.com/problems/happy-students/

#include <algorithm>
#include <vector>

class Solution {
public:
    int countWays(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size(), ans = 0;
        if (nums[0] > 0) ans++;
        for (int i = 0; i < n; i++) {
            int selected = i + 1;
            if (selected > nums[i] && (i == n - 1 || selected < nums[i + 1])) ans++;
        }
        return ans;
    }
};
