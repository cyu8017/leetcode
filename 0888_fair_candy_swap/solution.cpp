// LeetCode 0888 - Fair Candy Swap
// https://leetcode.com/problems/fair-candy-swap/

#include <numeric>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> fairCandySwap(std::vector<int>& aliceSizes,
                                   std::vector<int>& bobSizes) {
        int diff = (std::accumulate(aliceSizes.begin(), aliceSizes.end(), 0) -
                    std::accumulate(bobSizes.begin(), bobSizes.end(), 0)) /
                   2;
        std::unordered_set<int> bob(bobSizes.begin(), bobSizes.end());
        for (int a : aliceSizes) {
            if (bob.count(a - diff)) {
                return {a, a - diff};
            }
        }
        return {};
    }
};
