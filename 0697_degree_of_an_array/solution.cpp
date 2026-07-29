// LeetCode 0697 - Degree of an Array
// https://leetcode.com/problems/degree-of-an-array/

#include <algorithm>
#include <climits>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int findShortestSubArray(std::vector<int>& nums) {
        std::unordered_map<int, int> first;
        std::unordered_map<int, int> last;
        std::unordered_map<int, int> count;
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            if (!first.count(nums[i])) {
                first[nums[i]] = i;
            }
            last[nums[i]] = i;
            ++count[nums[i]];
        }
        int degree = 0;
        for (const auto& [_, freq] : count) {
            degree = std::max(degree, freq);
        }
        int best = INT_MAX;
        for (const auto& [num, freq] : count) {
            if (freq == degree) {
                best = std::min(best, last[num] - first[num] + 1);
            }
        }
        return best;
    }
};
