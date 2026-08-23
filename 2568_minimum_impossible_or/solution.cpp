// LeetCode 2568 - Minimum Impossible OR
// https://leetcode.com/problems/minimum-impossible-or/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int minImpossibleOR(std::vector<int>& nums) {
        std::unordered_set<int> set(nums.begin(), nums.end());
        for (int i = 1; ; i <<= 1) {
            if (!set.count(i)) return i;
        }
    }
};
