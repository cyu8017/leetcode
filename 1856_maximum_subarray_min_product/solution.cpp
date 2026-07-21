// LeetCode 1856 - Maximum Subarray Min-Product
// https://leetcode.com/problems/maximum-subarray-min-product/

#include <algorithm>
#include <stack>
#include <vector>

class Solution {
public:
    int maxSumMinProduct(std::vector<int>& nums) {
        const long long MOD = 1000000007LL;
        int n = static_cast<int>(nums.size());
        std::vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        std::vector<int> leftBound(n, -1);
        std::stack<int> stack;
        for (int i = 0; i < n; i++) {
            while (!stack.empty() && nums[stack.top()] >= nums[i]) {
                stack.pop();
            }
            leftBound[i] = stack.empty() ? -1 : stack.top();
            stack.push(i);
        }

        std::vector<int> rightBound(n, n);
        while (!stack.empty()) stack.pop();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.empty() && nums[stack.top()] >= nums[i]) {
                stack.pop();
            }
            rightBound[i] = stack.empty() ? n : stack.top();
            stack.push(i);
        }

        long long best = 0;
        for (int i = 0; i < n; i++) {
            long long total = prefix[rightBound[i]] - prefix[leftBound[i] + 1];
            best = std::max(best, total * nums[i]);
        }
        return static_cast<int>(best % MOD);
    }
};
