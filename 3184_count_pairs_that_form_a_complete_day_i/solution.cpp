// LeetCode 3184 - Count Pairs That Form a Complete Day I
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

#include <vector>
#include <array>

class Solution {
public:
    int countCompleteDayPairs(std::vector<int>& hours) {
        std::array<int, 24> cnt{};
        int ans = 0;
        for (int x : hours) {
            ans += cnt[(24 - x % 24) % 24];
            cnt[x % 24]++;
        }
        return ans;
    }
};
