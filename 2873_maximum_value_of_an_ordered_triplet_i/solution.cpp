// LeetCode 2873 - Maximum Value of an Ordered Triplet I
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

#include <vector>

class Solution {
public:
    long long maximumTripletValue(std::vector<int>& nums) {
        int n = (int)nums.size();
        long long ans = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                for (int k = j + 1; k < n; k++) {
                    long long cand = 1LL * (nums[i] - nums[j]) * nums[k];
                    if (cand > ans) ans = cand;
                }
        return ans;
    }
};
