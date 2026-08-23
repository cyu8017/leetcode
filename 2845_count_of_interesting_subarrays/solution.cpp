// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

#include <unordered_map>
#include <vector>

class Solution {
public:
    long long countInterestingSubarrays(std::vector<int>& nums, int modulo, int k) {
        std::unordered_map<int, int> freq{{0, 1}};
        long long ans = 0;
        int pref = 0;
        for (int v : nums) {
            if (v % modulo == k) pref++;
            int need = (pref - k) % modulo;
            if (need < 0) need += modulo;
            ans += freq[need];
            freq[pref % modulo]++;
        }
        return ans;
    }
};
