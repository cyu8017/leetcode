// LeetCode 2364 - Count Number of Bad Pairs
// https://leetcode.com/problems/count-number-of-bad-pairs/

#include <unordered_map>
#include <vector>

class Solution {
public:
    long long countBadPairs(std::vector<int>& nums) {
        long long n = nums.size();
        long long total = n * (n - 1) / 2;
        std::unordered_map<int, long long> freq;
        long long good = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            int key = nums[i] - i;
            good += freq[key];
            freq[key]++;
        }
        return total - good;
    }
};
