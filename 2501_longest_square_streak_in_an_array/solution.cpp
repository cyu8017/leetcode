// LeetCode 2501 - Longest Square Streak in an Array
// https://leetcode.com/problems/longest-square-streak-in-an-array/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int longestSquareStreak(std::vector<int>& nums) {
        std::unordered_set<long long> set(nums.begin(), nums.end());
        int best = -1;
        for (int x : nums) {
            if (!set.count(x)) continue;
            int length = 0;
            long long cur = x;
            while (set.count(cur)) {
                length++;
                set.erase(cur);
                if (cur > 100000) break;
                cur = cur * cur;
            }
            if (length >= 2 && length > best) best = length;
        }
        return best;
    }
};
