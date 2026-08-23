// LeetCode 3028 - Ant on the Boundary
// https://leetcode.com/problems/ant-on-the-boundary/

#include <vector>

class Solution {
public:
    int returnToBoundaryCount(std::vector<int>& nums) {
        int s = 0, ans = 0;
        for (int x : nums) {
            s += x;
            if (s == 0) ans++;
        }
        return ans;
    }
};
