// LeetCode 3261 - Count Substrings That Satisfy K-Constraint II
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

#include <cstdint>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<long long> countKConstraintSubstrings(std::string s, int k, std::vector<std::vector<int>>& queries) {
        int n = (int)s.size();
        std::vector<int> leftMost(n);
        int z = 0, o = 0, L = 0;
        for (int R = 0; R < n; R++) {
            if (s[R] == '0') z++; else o++;
            while (z > k && o > k) {
                if (s[L] == '0') z--; else o--;
                L++;
            }
            leftMost[R] = L;
        }
        std::vector<int64_t> pref(n + 1);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + (i - leftMost[i] + 1);
        std::vector<long long> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int l = queries[qi][0], r = queries[qi][1];
            int lo = l, hi = r + 1;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (leftMost[mid] < l) lo = mid + 1;
                else hi = mid;
            }
            int64_t res = 0;
            if (lo > l) {
                int64_t m = lo - l;
                res += m * (m + 1) / 2;
            }
            if (lo <= r) res += pref[r + 1] - pref[lo];
            ans[qi] = res;
        }
        return ans;
    }
};
