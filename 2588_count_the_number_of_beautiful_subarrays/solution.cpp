// LeetCode 2588 - Count the Number of Beautiful Subarrays
// https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

#include <unordered_map>
#include <vector>

class Solution {
public:
    long long beautifulSubarrays(std::vector<int>& nums) {
        std::unordered_map<int, int> freq{{0, 1}};
        int xorv = 0;
        long long ans = 0;
        for (int x : nums) {
            xorv ^= x;
            ans += freq[xorv];
            freq[xorv]++;
        }
        return ans;
    }
};
