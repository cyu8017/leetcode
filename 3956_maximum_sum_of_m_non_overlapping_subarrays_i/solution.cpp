// LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

#include <vector>

class Solution {
public:
    long long maxSum(std::vector<int>& nums, int m, int l, int r) {
        int n = (int)nums.size();
        std::vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        std::vector<long long> dp(n + 1, 0);
        long long bestSelected = -(1LL << 62);
        for (int count = 1; count <= m; count++) {
            std::vector<long long> next = dp;
            std::vector<int> deque;
            for (int end = 1; end <= n; end++) {
                int addIndex = end - l;
                if (addIndex >= 0) {
                    long long value = dp[addIndex] - prefix[addIndex];
                    while (!deque.empty()) {
                        int last = deque.back();
                        if (dp[last] - prefix[last] > value) break;
                        deque.pop_back();
                    }
                    deque.push_back(addIndex);
                }
                int minIndex = end - r;
                while (!deque.empty() && deque.front() < minIndex) deque.erase(deque.begin());
                if (!deque.empty()) {
                    long long candidate = prefix[end] + dp[deque.front()] - prefix[deque.front()];
                    if (candidate > next[end]) next[end] = candidate;
                    if (candidate > bestSelected) bestSelected = candidate;
                }
                if (next[end - 1] > next[end]) next[end] = next[end - 1];
            }
            dp.swap(next);
        }
        return bestSelected;
    }
};
