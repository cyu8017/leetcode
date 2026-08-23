// LeetCode 3139 - Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/

#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    int minCostToEqualizeArray(std::vector<int>& nums, int cost1, int cost2) {
        const int mod = 1000000007;
        int n = (int)nums.size();
        int minNum = nums[0], maxNum = nums[0];
        long long sum = 0;
        for (int v : nums) {
            minNum = std::min(minNum, v);
            maxNum = std::max(maxNum, v);
            sum += v;
        }
        if (cost1 * 2LL <= cost2 || n < 3) {
            long long totalGap = 1LL * maxNum * n - sum;
            return (int)(1LL * cost1 * totalGap % mod);
        }
        long long ans = LLONG_MAX;
        for (int target = maxNum; target < 2 * maxNum; target++) {
            int maxGap = target - minNum;
            long long totalGap = 1LL * target * n - sum;
            long long pairs = totalGap / 2;
            long long alt = totalGap - maxGap;
            if (alt < pairs) pairs = alt;
            long long cost = 1LL * cost1 * (totalGap - 2 * pairs) + 1LL * cost2 * pairs;
            ans = std::min(ans, cost);
        }
        return (int)(ans % mod);
    }
};
