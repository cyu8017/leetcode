// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

#include <string>
#include <vector>

class Solution {
public:
    int minTime(std::string s, std::vector<int>& order, int k) {
        int n = (int)s.size();
        long long total = 1LL * n * (n + 1) / 2;
        if (k > total) return -1;
        auto countValid = [&](int t) {
            std::vector<bool> star(n);
            for (int i = 0; i <= t; i++) star[order[i]] = true;
            long long invalid = 0;
            for (int i = 0; i < n;) {
                if (star[i]) {
                    i++;
                    continue;
                }
                int j = i;
                while (j < n && !star[j]) j++;
                long long L = j - i;
                invalid += L * (L + 1) / 2;
                i = j;
            }
            return total - invalid;
        };
        int lo = 0, hi = n - 1, ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (countValid(mid) >= k) {
                ans = mid;
                hi = mid - 1;
            } else lo = mid + 1;
        }
        return ans;
    }
};
