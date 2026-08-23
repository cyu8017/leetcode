// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long countTheNumOfKFreeSubsets(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        std::unordered_map<int, std::vector<int>> groups;
        for (int x : nums) groups[x % k].push_back(x);
        long long ans = 1;
        for (auto& [_, g] : groups) {
            int prevVal = -1;
            long long prevTake = 0, prevSkip = 1;
            for (int v : g) {
                long long take = 0, skip = prevTake + prevSkip;
                if (prevVal + k == v) take = prevSkip;
                else take = prevTake + prevSkip;
                prevTake = take;
                prevSkip = skip;
                prevVal = v;
            }
            ans *= prevTake + prevSkip;
        }
        return ans;
    }
};
