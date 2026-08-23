// LeetCode 3411 - Maximum Subarray With Equal Products
// https://leetcode.com/problems/maximum-subarray-with-equal-products/

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
    int maxLength(std::vector<int>& nums) {
        int n = (int)nums.size();
        int ans = 1;
        for (int i = 0; i < n; i++) {
            long long prod = 1;
            int g = 0, l = 1;
            for (int j = i; j < n; j++) {
                if (prod > 1000000000LL / nums[j]) break;
                prod *= nums[j];
                if (g == 0) {
                    g = nums[j];
                    l = nums[j];
                } else {
                    g = gcd(g, nums[j]);
                    l = l / gcd(l, nums[j]) * nums[j];
                }
                if (prod == (long long)l * g && j - i + 1 > ans) ans = j - i + 1;
            }
        }
        return ans;
    }
};
