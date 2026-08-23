// LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

#include <unordered_map>
#include <vector>

class Solution {
public:
    long long maximumSubarraySum(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> cnt;
        long long sum = 0, ans = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            sum += nums[i];
            cnt[nums[i]]++;
            if (i >= k) {
                int y = nums[i - k];
                sum -= y;
                if (--cnt[y] == 0) cnt.erase(y);
            }
            if (i >= k - 1 && (int)cnt.size() == k && sum > ans) ans = sum;
        }
        return ans;
    }
};
