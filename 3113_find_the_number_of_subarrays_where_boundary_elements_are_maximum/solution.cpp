// LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
// https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

#include <vector>

class Solution {
public:
    long long numberOfSubarrays(std::vector<int>& nums) {
        std::vector<std::pair<int, int>> stk;
        long long ans = 0;
        for (int x : nums) {
            while (!stk.empty() && stk.back().first < x) stk.pop_back();
            if (stk.empty() || stk.back().first > x) stk.push_back({x, 1});
            else stk.back().second++;
            ans += stk.back().second;
        }
        return ans;
    }
};
