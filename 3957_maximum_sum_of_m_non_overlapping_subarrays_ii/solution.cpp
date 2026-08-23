// LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

#include <vector>

class Solution {
    struct State {
        long long value = 0;
        int count = 0;
    };

    static bool better(State a, State b) {
        return a.value > b.value || (a.value == b.value && a.count > b.count);
    }

public:
    long long maxSum(std::vector<int>& nums, int m, int l, int r) {
        int n = (int)nums.size();
        std::vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

        auto run = [&](long long penalty) -> State {
            std::vector<State> dp(n + 1);
            std::vector<int> deque;
            auto candidateBetter = [&](int a, int b) {
                State left{dp[a].value - prefix[a], dp[a].count};
                State right{dp[b].value - prefix[b], dp[b].count};
                return better(left, right);
            };
            for (int end = 1; end <= n; end++) {
                int addIndex = end - l;
                if (addIndex >= 0) {
                    while (!deque.empty() && candidateBetter(addIndex, deque.back())) deque.pop_back();
                    deque.push_back(addIndex);
                }
                int minIndex = end - r;
                while (!deque.empty() && deque.front() < minIndex) deque.erase(deque.begin());
                dp[end] = dp[end - 1];
                if (!deque.empty()) {
                    int start = deque.front();
                    State take{dp[start].value + prefix[end] - prefix[start] - penalty, dp[start].count + 1};
                    if (better(take, dp[end])) dp[end] = take;
                }
            }
            return dp[n];
        };

        State unconstrained = run(0);
        if (unconstrained.count > 0 && unconstrained.count <= m) return unconstrained.value;
        if (unconstrained.count > m) {
            long long bound = 0;
            for (int value : nums) bound += value >= 0 ? value : -value;
            long long low = 0, high = bound + 1;
            while (low < high) {
                long long mid = low + (high - low + 1) / 2;
                if (run(mid).count >= m) low = mid;
                else high = mid - 1;
            }
            State state = run(low);
            return state.value + low * m;
        }
        const long long infinity = 1LL << 60;
        long long bestSingle = -infinity;
        std::vector<int> deque;
        for (int end = 1; end <= n; end++) {
            int addIndex = end - l;
            if (addIndex >= 0) {
                while (!deque.empty() && prefix[deque.back()] >= prefix[addIndex]) deque.pop_back();
                deque.push_back(addIndex);
            }
            int minIndex = end - r;
            while (!deque.empty() && deque.front() < minIndex) deque.erase(deque.begin());
            if (!deque.empty()) {
                long long sum = prefix[end] - prefix[deque.front()];
                if (sum > bestSingle) bestSingle = sum;
            }
        }
        return bestSingle;
    }
};
