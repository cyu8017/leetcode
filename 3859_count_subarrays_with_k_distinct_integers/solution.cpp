// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

#include <cstdint>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long countSubarrays(std::vector<int>& nums, int k, int m) {
        auto f = [&](int lim) {
            std::unordered_map<int, int> cnt;
            int64_t ans = 0;
            int l = 0, t = 0;
            for (int x : nums) {
                if (++cnt[x] == m) t++;
                while ((int)cnt.size() >= lim && t >= k) {
                    int y = nums[l++];
                    if (--cnt[y] == m - 1) t--;
                    if (cnt[y] == 0) cnt.erase(y);
                }
                ans += l;
            }
            return ans;
        };
        return f(k) - f(k + 1);
    }
};
