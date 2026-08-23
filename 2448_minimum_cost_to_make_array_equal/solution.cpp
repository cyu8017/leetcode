// LeetCode 2448 - Minimum Cost to Make Array Equal
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minCost(std::vector<int>& nums, std::vector<int>& cost) {
        int n = (int)nums.size();
        std::vector<int> idx(n);
        for (int i = 0; i < n; i++) idx[i] = i;
        std::sort(idx.begin(), idx.end(), [&](int a, int b) { return nums[a] < nums[b]; });
        long long totalCost = 0;
        for (int c : cost) totalCost += c;
        long long pref = 0;
        int median = 0;
        for (int i : idx) {
            pref += cost[i];
            if (pref * 2 >= totalCost) {
                median = nums[i];
                break;
            }
        }
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            long long diff = nums[i] - median;
            if (diff < 0) diff = -diff;
            ans += diff * cost[i];
        }
        return ans;
    }
};
