// LeetCode 3266 - Final Array State After K Multiplication Operations II
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

#include <cstdint>
#include <queue>
#include <utility>
#include <vector>

class Solution {
    long long modPow(long long a, long long e, long long mod) {
        long long r = 1;
        a %= mod;
        while (e > 0) {
            if (e & 1) r = r * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return r;
    }

public:
    std::vector<int> getFinalState(std::vector<int>& nums, int k, int multiplier) {
        const int mod = 1000000007;
        if (multiplier == 1) return nums;
        using P = std::pair<int, int>;
        std::priority_queue<P, std::vector<P>, std::greater<P>> h;
        int maxV = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            h.push({nums[i], i});
            if (nums[i] > maxV) maxV = nums[i];
        }
        while (k > 0 && !h.empty()) {
            auto [v, i] = h.top();
            h.pop();
            if ((int64_t)v * multiplier > maxV && k >= (int)nums.size()) {
                h.push({v, i});
                break;
            }
            int nv = v * multiplier;
            nums[i] = nv;
            if (nv > maxV) maxV = nv;
            h.push({nv, i});
            k--;
        }
        if (k > 0) {
            int n = (int)nums.size();
            int full = k / n, rem = k % n;
            long long powFull = modPow(multiplier, full, mod);
            for (int i = 0; i < n; i++) nums[i] = (int)((int64_t)nums[i] * powFull % mod);
            std::priority_queue<P, std::vector<P>, std::greater<P>> hh;
            for (int i = 0; i < n; i++) hh.push({nums[i], i});
            for (int t = 0; t < rem; t++) {
                auto [v, i] = hh.top();
                hh.pop();
                v = (int)((int64_t)v * multiplier % mod);
                nums[i] = v;
                hh.push({v, i});
            }
            for (int& x : nums) x %= mod;
        } else {
            for (int& x : nums) x %= mod;
        }
        return nums;
    }
};
