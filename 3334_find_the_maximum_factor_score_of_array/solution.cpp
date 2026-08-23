// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

#include <cstdint>
#include <vector>

class Solution {
    int gcd(int a, int b) {
        while (b) { int t = a % b; a = b; b = t; }
        return a;
    }
    int lcm(int a, int b) { return a / gcd(a, b) * b; }

public:
    long long maxScore(std::vector<int>& nums) {
        int n = (int)nums.size();
        int gcdAll = nums[0], lcmAll = nums[0];
        for (int i = 1; i < n; i++) {
            gcdAll = gcd(gcdAll, nums[i]);
            lcmAll = lcm(lcmAll, nums[i]);
        }
        long long ans = (long long)gcdAll * lcmAll;
        for (int skip = 0; skip < n; skip++) {
            int g = 0, l = 1;
            bool first = true;
            for (int i = 0; i < n; i++) {
                if (i == skip) continue;
                if (first) { g = l = nums[i]; first = false; }
                else { g = gcd(g, nums[i]); l = lcm(l, nums[i]); }
            }
            if (first) continue;
            long long v = (long long)g * l;
            if (v > ans) ans = v;
        }
        return ans;
    }
};
