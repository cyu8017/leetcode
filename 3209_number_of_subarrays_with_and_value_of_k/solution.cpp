// LeetCode 3209 - Number of Subarrays With AND Value of K
// https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

#include <vector>
#include <unordered_map>

class Solution {
public:
    long long countSubarrays(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> pre;
        long long ans = 0;
        for (int x : nums) {
            std::unordered_map<int, int> cur;
            for (auto& [y, v] : pre) cur[x & y] += v;
            cur[x]++;
            ans += cur[k];
            pre.swap(cur);
        }
        return ans;
    }
};
