// LeetCode 2367 - Number of Arithmetic Triplets
// https://leetcode.com/problems/number-of-arithmetic-triplets/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int arithmeticTriplets(std::vector<int>& nums, int diff) {
        std::unordered_set<int> seen(nums.begin(), nums.end());
        int ans = 0;
        for (int x : nums) {
            if (seen.count(x + diff) && seen.count(x + 2 * diff)) ans++;
        }
        return ans;
    }
};
