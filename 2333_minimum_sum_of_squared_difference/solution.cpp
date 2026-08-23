// LeetCode 2333 - Minimum Sum of Squared Difference
// https://leetcode.com/problems/minimum-sum-of-squared-difference/

#include <cmath>
#include <vector>
#include <algorithm>

class Solution {
public:
    long long minSumSquareDiff(std::vector<int>& nums1, std::vector<int>& nums2, int k1, int k2) {
        int n = (int)nums1.size();
        std::vector<int> diff(n);
        int maxD = 0;
        for (int i = 0; i < n; i++) {
            int d = std::abs(nums1[i] - nums2[i]);
            diff[i] = d;
            if (d > maxD) maxD = d;
        }
        int k = k1 + k2;
        std::vector<int> freq(maxD + 1);
        for (int d : diff) freq[d]++;
        for (int d = maxD; d > 0 && k > 0; d--) {
            if (freq[d] == 0) continue;
            int take = freq[d];
            if (take > k) take = k;
            freq[d] -= take;
            freq[d - 1] += take;
            k -= take;
        }
        long long ans = 0;
        for (int d = 0; d <= maxD; d++) {
            ans += 1LL * d * d * freq[d];
        }
        return ans;
    }
};
