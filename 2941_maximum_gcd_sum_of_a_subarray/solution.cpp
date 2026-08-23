// LeetCode 2941 - Maximum GCD-Sum of a Subarray
// https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

#include <numeric>
#include <vector>

class Solution {
public:
    long long maxGcdSum(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<long long> pref(n + 1);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        long long ans = 0;
        std::vector<std::pair<int, int>> st;
        for (int i = 0; i < n; i++) {
            std::vector<std::pair<int, int>> nst = {{nums[i], i}};
            for (auto [g0, idx] : st) {
                int g = std::gcd(g0, nums[i]);
                if (nst.back().first == g) continue;
                nst.push_back({g, idx});
            }
            st.swap(nst);
            for (auto [g, idx] : st) {
                if (i - idx + 1 >= k) {
                    long long cand = (pref[i + 1] - pref[idx]) * g;
                    if (cand > ans) ans = cand;
                }
            }
        }
        return ans;
    }
};
