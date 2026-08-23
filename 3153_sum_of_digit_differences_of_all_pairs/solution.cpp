// LeetCode 3153 - Sum of Digit Differences of All Pairs
// https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

#include <vector>
#include <cmath>

class Solution {
public:
    long long sumDigitDifferences(std::vector<int>& nums) {
        int n = (int)nums.size();
        int m = (int)std::floor(std::log10(nums[0])) + 1;
        long long ans = 0;
        for (int k = 0; k < m; k++) {
            int cnt[10] = {};
            for (int i = 0; i < n; i++) {
                cnt[nums[i] % 10]++;
                nums[i] /= 10;
            }
            for (int v : cnt) ans += 1LL * v * (n - v);
        }
        return ans / 2;
    }
};
