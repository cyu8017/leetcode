// LeetCode 3284 - Sum of Consecutive Subarrays
// https://leetcode.com/problems/sum-of-consecutive-subarrays/

#include <vector>

class Solution {
public:
    int rangeSum(std::vector<int>& nums) {
        const int mod = 1000000007;
        int n = (int)nums.size(), ans = 0, i = 0;
        while (i < n) {
            int j = i;
            while (j + 1 < n && (nums[j + 1] == nums[j] + 1 || nums[j + 1] == nums[j] - 1)) j++;
            for (int L = i; L <= j; L++) {
                int s = 0;
                for (int R = L; R <= j; R++) {
                    s += nums[R];
                    ans = (ans + s) % mod;
                }
            }
            i = j + 1;
        }
        return ans;
    }
};
