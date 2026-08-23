// LeetCode 2970 - Count the Number of Incremovable Subarrays I
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

#include <vector>

class Solution {
public:
    int incremovableSubarrayCount(std::vector<int>& nums) {
        int n = (int)nums.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int prev = -1;
                bool ok = true;
                for (int t = 0; t < n; t++) {
                    if (t >= i && t <= j) continue;
                    if (nums[t] <= prev) {
                        ok = false;
                        break;
                    }
                    prev = nums[t];
                }
                if (ok) ans++;
            }
        }
        return ans;
    }
};
