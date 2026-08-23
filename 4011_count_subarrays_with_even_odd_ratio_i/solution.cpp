// LeetCode 4011 - Count Subarrays With Even Odd Ratio I
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/

#include <cstdint>
#include <vector>

class Solution {
public:
    int countRatioSubarrays(std::vector<int>& nums, int a, int b) {
        int n = (int)nums.size();
        int64_t ans = 0;
        for (int i = 0; i < n; i++) {
            int y = 0;
            for (int j = i; j < n; j++) {
                y += nums[j] % 2;
                int x = j - i + 1 - y;
                if (y > 0 && (int64_t)x * (int64_t)b <= (int64_t)y * (int64_t)a) {
                    ans++;
                }
            }
        }
        return (int)ans;
    }
};
