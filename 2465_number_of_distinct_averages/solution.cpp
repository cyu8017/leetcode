// LeetCode 2465 - Number of Distinct Averages
// https://leetcode.com/problems/number-of-distinct-averages/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int distinctAverages(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::unordered_set<int> seen;
        int l = 0, r = (int)nums.size() - 1;
        while (l < r) {
            seen.insert(nums[l] + nums[r]);
            l++;
            r--;
        }
        return (int)seen.size();
    }
};
