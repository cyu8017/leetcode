// LeetCode 3185 - Count Pairs That Form a Complete Day II
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/

#include <vector>
#include <array>

class Solution {
public:
    long long countCompleteDayPairs(std::vector<int>& hours) {
        std::array<int, 24> cnt{};
        long long ans = 0;
        for (int x : hours) {
            ans += cnt[(24 - x % 24) % 24];
            cnt[x % 24]++;
        }
        return ans;
    }
};
