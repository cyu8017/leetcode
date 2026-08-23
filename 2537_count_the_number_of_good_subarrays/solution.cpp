// LeetCode 2537 - Count the Number of Good Subarrays
// https://leetcode.com/problems/count-the-number-of-good-subarrays/

#include <unordered_map>
#include <vector>

class Solution {
public:
    long long countGood(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> freq;
        long long pairs = 0, ans = 0;
        int left = 0;
        for (int right = 0; right < (int)nums.size(); right++) {
            pairs += freq[nums[right]];
            freq[nums[right]]++;
            while (pairs >= k) {
                ans += (int)nums.size() - right;
                freq[nums[left]]--;
                pairs -= freq[nums[left]];
                left++;
            }
        }
        return ans;
    }
};
