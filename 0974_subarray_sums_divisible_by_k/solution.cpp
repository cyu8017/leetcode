// LeetCode 0974 - Subarray Sums Divisible by K
// https://leetcode.com/problems/subarray-sums-divisible-by-k/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int subarraysDivByK(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> count;
        count[0] = 1;
        int prefix = 0, ans = 0;
        for (int x : nums) {
            prefix = ((prefix + x) % k + k) % k;
            ans += count[prefix];
            count[prefix]++;
        }
        return ans;
    }
};
