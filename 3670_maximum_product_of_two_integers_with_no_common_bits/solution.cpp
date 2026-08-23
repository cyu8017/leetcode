// LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
// https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long maxProduct(std::vector<int>& nums) {
        int maxV = 0;
        for (int v : nums) if (v > maxV) maxV = v;
        int bitsN = 0;
        for (int x = maxV; x > 0; x >>= 1) bitsN++;
        if (bitsN == 0) bitsN = 1;
        int size = 1 << bitsN;
        std::vector<int> best(size, 0);
        for (int v : nums) if (v > best[v]) best[v] = v;
        for (int mask = 0; mask < size; mask++) {
            for (int b = 0; b < bitsN; b++) {
                if (mask & (1 << b)) {
                    int sub = mask ^ (1 << b);
                    if (best[sub] > best[mask]) best[mask] = best[sub];
                }
            }
        }
        long long ans = 0;
        for (int v : nums) {
            int comp = (size - 1) ^ v;
            if (best[comp] > 0) {
                long long p = (long long)v * best[comp];
                if (p > ans) ans = p;
            }
        }
        return ans;
    }
};
