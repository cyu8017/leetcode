// LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long countValidSubarrays(std::vector<int>& nums, int x) {
        std::vector<std::vector<long long>> byRemainder(10);
        byRemainder[0].push_back(0);
        long long prefix = 0, answer = 0;
        for (int value : nums) {
            prefix += value;
            int required = (int)((prefix - x) % 10 + 10) % 10;
            auto& values = byRemainder[required];
            for (long long power = 1; (long long)x * power <= prefix; power *= 10) {
                long long low = (long long)x * power;
                long long high = (long long)(x + 1) * power - 1;
                long long minPrefix = prefix - high, maxPrefix = prefix - low;
                auto left = std::lower_bound(values.begin(), values.end(), minPrefix);
                auto right = std::upper_bound(values.begin(), values.end(), maxPrefix);
                answer += right - left;
                if (power > prefix / 10) break;
            }
            byRemainder[(int)(prefix % 10)].push_back(prefix);
        }
        return answer;
    }
};
