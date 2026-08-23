// LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    long long minOperations(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        if (k == 0) return 0;
        if (k > n / 2) return -1;
        std::vector<long long> cost(n, 0);
        for (int i = 0; i < n; i++) {
            int left = nums[(i + n - 1) % n], right = nums[(i + 1) % n];
            int need = std::max(left, right);
            if (need >= nums[i]) cost[i] = (long long)need - nums[i] + 1;
        }
        const long long inf = 1LL << 60;

        auto line = [&](int left, int right, int choose) -> long long {
            if (choose == 0) return 0;
            if (left > right || choose > (right - left + 2) / 2) return inf;
            std::vector<long long> prev2(choose + 1, inf), prev1(choose + 1, inf);
            prev2[0] = prev1[0] = 0;
            for (int i = left; i <= right; i++) {
                std::vector<long long> current = prev1;
                for (int j = 1; j <= choose; j++) {
                    if (prev2[j - 1] != inf && prev2[j - 1] + cost[i] < current[j]) {
                        current[j] = prev2[j - 1] + cost[i];
                    }
                }
                prev2.swap(prev1);
                prev1.swap(current);
            }
            return prev1[choose];
        };

        long long answer = line(1, n - 1, k);
        long long withFirst = line(2, n - 2, k - 1);
        if (withFirst != inf) {
            withFirst += cost[0];
            answer = std::min(answer, withFirst);
        }
        if (answer == inf) return -1;
        return answer;
    }
};
