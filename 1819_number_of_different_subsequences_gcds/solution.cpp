// LeetCode 1819 - Number of Different Subsequences GCDs
// https://leetcode.com/problems/number-of-different-subsequences-gcds/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int countDifferentSubsequenceGCDs(std::vector<int>& nums) {
        int maxVal = *std::max_element(nums.begin(), nums.end());
        std::vector<char> present(maxVal + 1, 0);
        for (int num : nums) {
            present[num] = 1;
        }
        int ans = 0;
        for (int g = 1; g <= maxVal; ++g) {
            bool has = false;
            int gcdVal = 0;
            for (int multiple = g; multiple <= maxVal; multiple += g) {
                if (present[multiple]) {
                    has = true;
                    gcdVal = std::gcd(gcdVal, multiple / g);
                    if (gcdVal == 1) {
                        break;
                    }
                }
            }
            if (has && gcdVal == 1) {
                ++ans;
            }
        }
        return ans;
    }
};
