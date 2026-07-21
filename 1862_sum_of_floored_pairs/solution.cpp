// LeetCode 1862 - Sum of Floored Pairs
// https://leetcode.com/problems/sum-of-floored-pairs/

#include <algorithm>
#include <vector>

class Solution {
public:
    int sumOfFlooredPairs(std::vector<int>& nums) {
        const int MOD = 1000000007;
        int maxVal = *std::max_element(nums.begin(), nums.end());
        std::vector<int> count(maxVal + 1, 0);
        for (int num : nums) {
            count[num]++;
        }
        std::vector<long long> prefix(maxVal + 1, 0);
        prefix[0] = count[0];
        for (int value = 1; value <= maxVal; value++) {
            prefix[value] = prefix[value - 1] + count[value];
        }

        long long answer = 0;
        for (int divisor = 1; divisor <= maxVal; divisor++) {
            if (count[divisor] == 0) continue;
            int quotient = 1;
            while (1LL * quotient * divisor <= maxVal) {
                int low = quotient * divisor;
                int high = std::min((quotient + 1) * divisor - 1, maxVal);
                long long matches = prefix[high] - (low ? prefix[low - 1] : 0);
                answer = (answer + count[divisor] * matches * quotient) % MOD;
                quotient++;
            }
        }
        return static_cast<int>(answer);
    }
};
