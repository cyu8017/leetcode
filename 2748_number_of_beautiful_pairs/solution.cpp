// LeetCode 2748 - Number of Beautiful Pairs
// https://leetcode.com/problems/number-of-beautiful-pairs/

#include <vector>
#include <numeric>

class Solution {
public:
    int countBeautifulPairs(std::vector<int>& nums) {
        int ans = 0;
        int freq[10] = {};
        auto firstDigit = [](int x) { while (x >= 10) x /= 10; return x; };
        for (int x : nums) {
            int last = x % 10;
            for (int d = 1; d <= 9; d++)
                if (freq[d] > 0 && std::gcd(d, last) == 1) ans += freq[d];
            freq[firstDigit(x)]++;
        }
        return ans;
    }
};
