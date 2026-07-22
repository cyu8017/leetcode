// LeetCode 1608 - Special Array With X Elements Greater Than or Equal X
// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

#include <vector>

class Solution {
public:
    int specialArray(std::vector<int>& nums) {
        const int n = static_cast<int>(nums.size());
        for (int x = 0; x <= n; ++x) {
            int cnt = 0;
            for (int v : nums) {
                if (v >= x) {
                    ++cnt;
                }
            }
            if (cnt == x) {
                return x;
            }
        }
        return -1;
    }
};
