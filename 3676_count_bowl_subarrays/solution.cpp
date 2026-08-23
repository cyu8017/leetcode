// LeetCode 3676 - Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/

#include <vector>

class Solution {
public:
    long long bowlSubarrays(std::vector<int>& nums) {
        int n = (int)nums.size();
        long long ans = 0;
        std::vector<int> ngr(n, -1), ngl(n, -1), stack;
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.empty() && nums[stack.back()] < nums[i]) stack.pop_back();
            if (!stack.empty()) ngr[i] = stack.back();
            stack.push_back(i);
        }
        stack.clear();
        for (int i = 0; i < n; i++) {
            while (!stack.empty() && nums[stack.back()] < nums[i]) stack.pop_back();
            if (!stack.empty()) ngl[i] = stack.back();
            stack.push_back(i);
        }
        for (int i = 0; i < n; i++) {
            if (ngr[i] != -1 && ngr[i] - i >= 2) ans++;
            if (ngl[i] != -1 && i - ngl[i] >= 2) ans++;
        }
        return ans;
    }
};
