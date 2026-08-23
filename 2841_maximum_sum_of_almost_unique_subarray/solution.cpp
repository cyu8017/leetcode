// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

#include <unordered_map>
#include <vector>
#include <algorithm>

class Solution {
public:
    long long maxSum(std::vector<int>& nums, int m, int k) {
        std::unordered_map<int, int> freq;
        long long sum = 0, ans = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            freq[nums[i]]++;
            sum += nums[i];
            if (i >= k) {
                int out = nums[i - k];
                sum -= out;
                if (--freq[out] == 0) freq.erase(out);
            }
            if (i >= k - 1 && (int)freq.size() >= m) ans = std::max(ans, sum);
        }
        return ans;
    }
};
