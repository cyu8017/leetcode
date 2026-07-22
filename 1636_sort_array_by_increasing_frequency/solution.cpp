// LeetCode 1636 - Sort Array by Increasing Frequency
// https://leetcode.com/problems/sort-array-by-increasing-frequency/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> frequencySort(std::vector<int>& nums) {
        std::unordered_map<int, int> count;
        for (int x : nums) {
            ++count[x];
        }
        std::sort(nums.begin(), nums.end(), [&](int a, int b) {
            if (count[a] != count[b]) {
                return count[a] < count[b];
            }
            return a > b;
        });
        return nums;
    }
};
