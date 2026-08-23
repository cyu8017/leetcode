// LeetCode 2475 - Number of Unequal Triplets in Array
// https://leetcode.com/problems/number-of-unequal-triplets-in-array/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int unequalTriplets(std::vector<int>& nums) {
        std::unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        int ans = 0, n = (int)nums.size(), left = 0;
        for (auto& [x, c] : cnt) {
            (void)x;
            int right = n - left - c;
            ans += left * c * right;
            left += c;
        }
        return ans;
    }
};
