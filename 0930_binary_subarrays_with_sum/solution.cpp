// LeetCode 0930 - Binary Subarrays With Sum
// https://leetcode.com/problems/binary-subarrays-with-sum/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int numSubarraysWithSum(std::vector<int>& nums, int goal) {
        std::unordered_map<int, int> count;
        count[0] = 1;
        int prefix = 0, ans = 0;
        for (int x : nums) {
            prefix += x;
            ans += count[prefix - goal];
            count[prefix]++;
        }
        return ans;
    }
};
