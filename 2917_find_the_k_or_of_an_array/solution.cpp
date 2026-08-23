// LeetCode 2917 - Find the K-or of an Array
// https://leetcode.com/problems/find-the-k-or-of-an-array/

#include <vector>

class Solution {
public:
    int findKOr(std::vector<int>& nums, int k) {
        int ans = 0;
        for (int b = 0; b < 31; b++) {
            int cnt = 0;
            for (int v : nums) if (v & (1 << b)) cnt++;
            if (cnt >= k) ans |= 1 << b;
        }
        return ans;
    }
};
