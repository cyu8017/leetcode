// LeetCode 3300 - Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

#include <vector>

class Solution {
public:
    int minElement(std::vector<int>& nums) {
        int ans = 1000000000;
        for (int x : nums) {
            int s = 0;
            while (x > 0) { s += x % 10; x /= 10; }
            if (s < ans) ans = s;
        }
        return ans;
    }
};
