// LeetCode 3199 - Count Triplets with Even XOR Set Bits I
// https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/

#include <vector>
#include <array>

class Solution {
public:
    int tripletCount(std::vector<int>& a, std::vector<int>& b, std::vector<int>& c) {
        std::array<int, 2> cnt1{}, cnt2{}, cnt3{};
        for (int x : a) cnt1[__builtin_popcount((unsigned)x) % 2]++;
        for (int x : b) cnt2[__builtin_popcount((unsigned)x) % 2]++;
        for (int x : c) cnt3[__builtin_popcount((unsigned)x) % 2]++;
        int ans = 0;
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                for (int k = 0; k < 2; k++)
                    if ((i + j + k) % 2 == 0) ans += cnt1[i] * cnt2[j] * cnt3[k];
        return ans;
    }
};
