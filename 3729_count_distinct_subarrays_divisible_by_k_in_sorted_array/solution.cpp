// LeetCode 3729 - Count Distinct Subarrays Divisible by K in Sorted Array
// https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

#include <unordered_map>
#include <vector>

class Solution {
public:
    long long numGoodSubarrays(std::vector<int>& nums, int k) {
        long long ans = 0;
        int s = 0;
        std::unordered_map<int, int> cnt{{0, 1}};
        for (int x : nums) {
            s = (s + x) % k;
            ans += cnt[s];
            cnt[s]++;
        }
        int n = (int)nums.size();
        for (int i = 0; i < n; ) {
            int j = i + 1;
            while (j < n && nums[j] == nums[i]) j++;
            int m = j - i;
            for (int h = 1; h <= m; h++) {
                if (1LL * nums[i] * h % k == 0) ans -= (m - h);
            }
            i = j;
        }
        return ans;
    }
};
