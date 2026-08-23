// LeetCode 3012 - Minimize Length of Array Using Operations
// https://leetcode.com/problems/minimize-length-of-array-using-operations/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minimumArrayLength(std::vector<int>& nums) {
        int mi = *std::min_element(nums.begin(), nums.end());
        int cnt = 0;
        for (int x : nums) {
            if (x % mi != 0) return 1;
            if (x == mi) cnt++;
        }
        return (cnt + 1) / 2;
    }
};
