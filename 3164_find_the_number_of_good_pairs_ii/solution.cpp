// LeetCode 3164 - Find the Number of Good Pairs II
// https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    long long numberOfPairs(std::vector<int>& nums1, std::vector<int>& nums2, int k) {
        std::unordered_map<int, int> cnt1;
        for (int x : nums1) if (x % k == 0) cnt1[x / k]++;
        if (cnt1.empty()) return 0;
        std::unordered_map<int, int> cnt2;
        for (int x : nums2) cnt2[x]++;
        int mx = 0;
        for (auto& [x, _] : cnt1) mx = std::max(mx, x);
        long long ans = 0;
        for (auto& [x, v] : cnt2) {
            int s = 0;
            for (int y = x; y <= mx; y += x) {
                auto it = cnt1.find(y);
                if (it != cnt1.end()) s += it->second;
            }
            ans += 1LL * s * v;
        }
        return ans;
    }
};
