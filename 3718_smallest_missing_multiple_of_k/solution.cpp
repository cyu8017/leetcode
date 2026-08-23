// LeetCode 3718 - Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int missingMultiple(std::vector<int>& nums, int k) {
        std::unordered_set<int> s(nums.begin(), nums.end());
        for (int i = 1;; i++) {
            int x = k * i;
            if (!s.count(x)) return x;
        }
    }
};
