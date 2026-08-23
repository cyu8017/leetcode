// LeetCode 2750 - Ways to Split Array Into Good Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

#include <vector>

class Solution {
public:
    int numberOfGoodSubarraySplits(std::vector<int>& nums) {
        const int MOD = 1000000007;
        std::vector<int> ones;
        for (int i = 0; i < (int)nums.size(); i++) if (nums[i] == 1) ones.push_back(i);
        if (ones.empty()) return 0;
        long long ans = 1;
        for (int i = 1; i < (int)ones.size(); i++)
            ans = ans * (ones[i] - ones[i - 1]) % MOD;
        return (int)ans;
    }
};
