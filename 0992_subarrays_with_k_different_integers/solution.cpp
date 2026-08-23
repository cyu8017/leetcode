// LeetCode 0992 - Subarrays with K Different Integers
// https://leetcode.com/problems/subarrays-with-k-different-integers/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int subarraysWithKDistinct(std::vector<int>& nums, int k) {
        auto atMost = [&](int m) {
            if (m < 0) return 0;
            std::unordered_map<int, int> count;
            int left = 0, ans = 0;
            for (int right = 0; right < (int)nums.size(); right++) {
                count[nums[right]]++;
                while ((int)count.size() > m) {
                    if (--count[nums[left]] == 0) count.erase(nums[left]);
                    left++;
                }
                ans += right - left + 1;
            }
            return ans;
        };
        return atMost(k) - atMost(k - 1);
    }
};
