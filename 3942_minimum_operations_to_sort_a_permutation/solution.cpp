// LeetCode 3942 - Minimum Operations To Sort A Permutation
// https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        int n = (int)nums.size();
        int zero = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                zero = i;
                break;
            }
        }
        auto check = [&](int step) {
            for (int i = 1; i < n; i++) {
                int prev = ((zero + (i - 1) * step) % n + n) % n;
                int curr = ((zero + i * step) % n + n) % n;
                if (nums[prev] > nums[curr]) return false;
            }
            return true;
        };
        int ans = INT_MAX;
        if (check(1)) {
            ans = std::min(ans, zero);
            ans = std::min(ans, n - zero + 2);
        }
        if (check(-1)) {
            ans = std::min(ans, zero + 2);
            ans = std::min(ans, n - zero);
        }
        if (ans == INT_MAX) return -1;
        return ans;
    }
};
