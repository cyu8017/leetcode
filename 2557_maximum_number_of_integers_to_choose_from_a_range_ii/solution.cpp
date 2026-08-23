// LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxCount(std::vector<int>& banned, int n, long long maxSum) {
        std::sort(banned.begin(), banned.end());
        std::vector<int> uniq;
        for (int x : banned) {
            if (x >= 1 && x <= n && (uniq.empty() || uniq.back() != x)) uniq.push_back(x);
        }
        int ans = 0;
        int prev = 0;
        long long remain = maxSum;
        auto check = [&](long long l, long long r) {
            if (l > r || remain <= 0) return;
            long long lo = l, hi = r, best = l - 1;
            while (lo <= hi) {
                long long mid = (lo + hi) / 2;
                long long cnt = mid - l + 1;
                long long sum = (l + mid) * cnt / 2;
                if (sum <= remain) {
                    best = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
            if (best >= l) {
                int cnt = (int)(best - l + 1);
                ans += cnt;
                remain -= (l + best) * cnt / 2;
            }
        };
        for (int b : uniq) {
            check((long long)prev + 1, (long long)b - 1);
            prev = b;
        }
        check((long long)prev + 1, (long long)n);
        return ans;
    }
};
