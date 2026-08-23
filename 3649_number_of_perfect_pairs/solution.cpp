// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

#include <algorithm>
#include <cmath>
#include <vector>

class Solution {
public:
    long long perfectPairs(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> absNums(n);
        for (int i = 0; i < n; i++) absNums[i] = std::abs(nums[i]);
        std::sort(absNums.begin(), absNums.end());
        long long ans = 0;
        int j = 0;
        for (int i = 0; i < n; i++) {
            if (j < i + 1) j = i + 1;
            while (j < n && absNums[j] <= 2 * absNums[i]) j++;
            ans += j - i - 1;
        }
        return ans;
    }
};
