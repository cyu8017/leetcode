// LeetCode 2233 - Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/

#include <vector>
#include <queue>

class Solution {
public:
    int maximumProduct(std::vector<int>& nums, int k) {
        const int MOD = 1000000007;
        std::priority_queue<int, std::vector<int>, std::greater<int>> h(nums.begin(), nums.end());
        for (int i = 0; i < k; ++i) {
            int x = h.top() + 1;
            h.pop();
            h.push(x);
        }
        long long ans = 1;
        while (!h.empty()) {
            ans = ans * h.top() % MOD;
            h.pop();
        }
        return (int)ans;
    }
};
