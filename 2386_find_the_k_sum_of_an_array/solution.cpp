// LeetCode 2386 - Find the K-Sum of an Array
// https://leetcode.com/problems/find-the-k-sum-of-an-array/

#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>

class Solution {
public:
    long long kSum(std::vector<int>& nums, int k) {
        long long total = 0;
        std::vector<int> absNums(nums.size());
        for (int i = 0; i < (int)nums.size(); i++) {
            if (nums[i] >= 0) {
                total += nums[i];
                absNums[i] = nums[i];
            } else {
                absNums[i] = -nums[i];
            }
        }
        std::sort(absNums.begin(), absNums.end());
        using P = std::pair<long long, int>;
        std::priority_queue<P> h;
        h.push({total, 0});
        for (int t = 0; t < k - 1; t++) {
            auto [sum, i] = h.top();
            h.pop();
            if (i >= (int)absNums.size()) continue;
            h.push({sum - absNums[i], i + 1});
            if (i > 0) {
                h.push({sum - absNums[i] + absNums[i - 1], i + 1});
            }
        }
        return h.top().first;
    }
};
