// LeetCode 2607 - Make K-Subarray Sums Equal
// https://leetcode.com/problems/make-k-subarray-sums-equal/

#include <algorithm>
#include <cstdlib>
#include <numeric>
#include <vector>

class Solution {
public:
    long long makeSubKSumEqual(std::vector<int>& arr, int k) {
        int n = (int)arr.size();
        int g = std::gcd(n, k);
        long long ans = 0;
        for (int r = 0; r < g; ++r) {
            std::vector<int> group;
            for (int i = r; i < n; i += g) group.push_back(arr[i]);
            std::sort(group.begin(), group.end());
            int med = group[group.size() / 2];
            for (int x : group) ans += std::abs(x - med);
        }
        return ans;
    }
};
