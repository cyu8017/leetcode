// LeetCode 2967 - Minimum Cost to Make Array Equalindromic
// https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>

class Solution {
public:
    long long minimumCost(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        int median = nums[n / 2];
        auto makePal = [](int x) -> int {
            std::string s = std::to_string(x);
            for (int i = 0, j = (int)s.size() - 1; i < j; i++, j--) s[j] = s[i];
            return std::stoi(s);
        };
        std::vector<int> candidates;
        int base = makePal(median);
        candidates.push_back(base);
        std::string s = std::to_string(median);
        int half = std::stoi(s.substr(0, (s.size() + 1) / 2));
        for (int d = -2; d <= 2; d++) {
            int h = half + d;
            if (h <= 0) continue;
            std::string hs = std::to_string(h);
            std::string pal;
            if (s.size() % 2 == 0) {
                std::string rb = hs;
                std::reverse(rb.begin(), rb.end());
                pal = hs + rb;
            } else {
                std::string rb = hs.substr(0, hs.size() - 1);
                std::reverse(rb.begin(), rb.end());
                pal = hs + rb;
            }
            try {
                candidates.push_back(std::stoi(pal));
            } catch (...) {
            }
        }
        for (int v : {1, 9, 11, 99, 101}) candidates.push_back(v);
        auto cost = [&](int p) -> long long {
            long long c = 0;
            for (int v : nums) c += std::llabs((long long)v - p);
            return c;
        };
        long long ans = (1LL << 62);
        for (int p : candidates) {
            if (p <= 0) continue;
            ans = std::min(ans, cost(p));
        }
        return ans;
    }
};
