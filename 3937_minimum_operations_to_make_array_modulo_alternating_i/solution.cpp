// LeetCode 3937 - Minimum Operations To Make Array Modulo Alternating I
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

#include <algorithm>
#include <climits>
#include <cmath>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        for (int& v : nums) v %= k;
        int ans = INT_MAX;
        for (int x = 0; x < k; x++) {
            for (int y = 0; y < k; y++) {
                if (x == y) continue;
                int cnt = 0;
                for (int i = 0; i < (int)nums.size(); i++) {
                    int target = (i & 1) ? y : x;
                    int diff = std::abs(target - nums[i]);
                    cnt += std::min(diff, k - diff);
                }
                ans = std::min(ans, cnt);
            }
        }
        return ans;
    }
};
