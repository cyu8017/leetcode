// LeetCode 3867 - Sum Of Gcd Of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
    static int gcd(int a, int b) {
        while (b) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

public:
    long long gcdSum(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> prefixGcd(n);
        int mx = 0;
        for (int i = 0; i < n; i++) {
            mx = std::max(mx, nums[i]);
            prefixGcd[i] = gcd(nums[i], mx);
        }
        std::sort(prefixGcd.begin(), prefixGcd.end());
        int64_t ans = 0;
        for (int i = 0; i < n / 2; i++) ans += gcd(prefixGcd[i], prefixGcd[n - i - 1]);
        return ans;
    }
};
